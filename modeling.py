import cPickle as pickle
import sys
import json
import pandas as pd
import nltk, string
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from FeedRSS import feedReader

roles = [['ice_director', 'mexico mexican drug smuggling border cartel'],
        ['md_syria', 'syria syrian refugee refugees camps', ],
        ['nkpg', 'north korea']]

stemmer = SnowballStemmer('english')
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

# remove punctuation, lowercase
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

def calculate_cosine_similarity(doc1, doc2):
    vect = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = vect.fit_transform([doc1, doc2])
    return (tfidf * tfidf.T).A

def obtain_rss_feeds():
    feeds = feedReader()

    labels = ['title', 'summary', 'link']
    return pd.DataFrame.from_records(feeds, columns=labels)

def format_df_all(news_feeds):
    labels = ['title', 'summary', 'link']
    df = pd.DataFrame.from_records(news_feeds, columns=labels)
    for role in roles:
        df[role[0]] = 0

    for i in xrange(len(df)):
        new_summary = df.iloc[i, 1].split('<')[0]
        df.set_value(i, 'summary', new_summary)

    vect = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    terms_list = [role[1] for role in roles]

    for i in xrange(len(df)):
        title = df.iloc[i]['title']
        tfidf = vect.fit_transform([title, terms_list[0], terms_list[1], terms_list[2]])
        df.iloc[i,-3:] = (tfidf * tfidf.T).A[0][1:]

    for role in roles:
        df['y_'+ role[0]] = 0


def format_df_one(news_feeds, advisor):
    labels = ['title', 'summary', 'link']
    df = pd.DataFrame.from_records(news_feeds, columns=labels)
    for i in xrange(len(df)):
        new_summary = df.iloc[i, 1].split('<')[0]
        df.set_value(i, 'summary', new_summary)

    vect = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    terms = [role[1] for role in roles if role[0] == advisor][0]

    df['similarity'] = 0
    for i in xrange(len(df)):
        title = df.iloc[i]['title']
        tfidf = vect.fit_transform([title, terms])
        df.iloc[i,-1] = (tfidf * tfidf.T).A[0][1:]
    return df

def build_MultinomialNB(df):
    ### code to build a NB model for each role to be run for only the first time

    positive_threshold = 0.05 # pretty low threshold which can be changed in the future
    for i in xrange(len(df)):
        if df.iloc[i][3] > positive_threshold:
            df.set_value(i, 'y_ice_director', 1) 
        if df.iloc[i][4] > positive_threshold:
            df.set_value(i, 'y_md_syria', 1) 
        if df.iloc[i][5] > positive_threshold:
            df.set_value(i, 'y_nkpg', 1) 

    X = df['title'] + df['summary']
    y_ice = df['y_ice_director']
    y_md_syria = df['y_md_syria']
    y_nkpg = df['y_nkpg']
    count_vectorizer = CountVectorizer(stop_words='english')
    cv = count_vectorizer.fit_transform(X)

    ice_director_nb = MultinomialNB()
    md_syria_nb = MultinomialNB()
    nkpg_nb = MultinomialNB()

    ice_director_nb.fit(cv, y_ice)
    md_syria_nb.fit(cv, y_md_syria)
    nkpg_nb.fit(cv, y_nkpg)
    return count_vectorizer, ice_director_nb, md_syria_nb, nkpg_nb

def predict(df, advisor, limit=10):
    if advisor == 'ice_director':
        model = 'ice_director_nb'
    elif advisor == 'md_syria':
        model = 'md_syria_nb'
    elif advisor == 'nkpg':
        model = 'nkpg_nb'
    else:
        return "Could not find advisor role. Options are ice_director, md_syria, or nkpg" 
    with open('models/' + model + '.pkl') as f:
        nb_model = pickle.load(f)

    X = df['title'] + df['summary']    
    tf = count_vectorizer.transform(X)
    df['y'] = nb_model.predict(tf)
    df = df[df['y'] == 1]
    df.drop_duplicates(subset='title', inplace=True)

    df.sort_values(by='similarity', inplace=True, ascending=False)
    df = df.iloc[:limit,]
    df.to_csv('data/' + advisor + '_results.csv', index=False, encoding='utf-8', sep='|')

def add_and_retrain_model(feedback, advisor):
    ''' Models are currently being retrain on data/training_data.csv and whatever articles receiving feedback.
    Articles with feedback are added to the training set. If/when the training set gets large (> 1M entries), 
    partial_fit can be used to train in batches. It would take a while for this to occur, so it is not here.
    '''

    update_col = 'y_' + advisor
    training = pd.read_csv('data/training_data.csv')

    for item in feedback:
        title = item['title']
        to_update = training[training['title'] == title].index.tolist()
        for ix in to_update:
            training.set_value(ix, update_col, item['like'])

    with open('models/ice_director_nb.pkl') as f:
        ice_director_nb = pickle.load(f)
    with open('models/md_syria_nb.pkl') as f:
        md_syria_nb = pickle.load(f)
    with open('models/nkpg_nb.pkl') as f:
        nkpg_nb = pickle.load(f)

    X = training['title'] + training['summary']
    y_ice = training['y_ice_director']
    y_md_syria = training['y_md_syria']
    y_nkpg = training['y_nkpg']
    count_vectorizer = CountVectorizer(stop_words='english')
    tf = count_vectorizer.fit_transform(X)
    ice_director_nb.fit(tf, y_ice)
    md_syria_nb.fit(tf, y_md_syria)
    nkpg_nb.fit(tf, y_nkpg)

    training.to_csv("data/training_data.csv", index=False, encoding='utf-8')
    with open('models/count_vectorizer.pkl', 'w') as f:
        pickle.dump(count_vectorizer, f)
    with open('models/ice_director_nb.pkl', 'w') as f:
        pickle.dump(ice_director_nb, f)
    with open('models/md_syria_nb.pkl', 'w') as f:
        pickle.dump(md_syria_nb, f)
    with open('models/nkpg_nb.pkl', 'w') as f:
        pickle.dump(nkpg_nb, f)

def retrieve_news(advisor):
    with open('models/count_vectorizer.pkl') as f:
        count_vectorizer = pickle.load(f)
        news_feeds = feedReader()
        news_df = format_df_one(news_feeds, advisor)
        predict(news_df, advisor)

def analyze_feedback(feedback, advisor):
    data = json.loads(feedback) 
    add_and_retrain_model(data, advisor)

# if __name__ == '__main__':
#     with open('models/count_vectorizer.pkl') as f:
#         count_vectorizer = pickle.load(f)
#     if len(sys.argv) == 2: # only run model, return results
#         advisor = sys.argv[1]
#         news_feeds = feedReader()
#         news_df = format_df_one(news_feeds, advisor)
#         predict(news_df, advisor)

#     elif len(sys.argv) == 3: # retrain model, no return
#         advisor = sys.argv[1]
#         feedback = sys.argv[2]
#         data = json.loads(feedback) 
#         add_and_retrain_model(data, advisor)


