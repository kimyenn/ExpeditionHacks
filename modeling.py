import cPickle as pickle
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
    print feeds
    return pd.DataFrame.from_records(feeds, columns=labels)

def format_df(df):
    for role in roles:
        df[role[0]] = 0

    vect = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    terms_list = [role[1] for role in roles]

    for i in xrange(len(df)):
        title = df.iloc[i]['title']
        tfidf = vect.fit_transform([title, terms_list[0], terms_list[1], terms_list[2]])
        df.iloc[i,-3:] = (tfidf * tfidf.T).A[0][1:]

    for role in roles:
        df['y_'+ role[0]] = 0

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
        model = ice_director_nb
    elif advisor == 'md_syria':
        model = md_syria_nb
    elif advisor == 'nkpg':
        model = nkpg_nb
    else:
        return "Could not find advisor role. Options are ice_director, md_syria, or nkpg" 
    with open('../data/count_vectorizer.pkl') as f:
        count_vectorizer = pickle.load(f)
    with open('../data/' + model + '.pkl') as f:
        model = pickle.load(f)

    data = df['title'] + df['summary']    
    X = count_vectorizer.fit_transform(data)
    predictions = model.predict(X)
    df['predictions'] = predictions
    df = df[df['predictions'] == 1]

    vect = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    terms_list = [role[1] for role in roles if role==advisor]
    df['similarity']
    for i in xrange(len(df)):
        title = df.iloc[i]['title']
        tfidf = vect.fit_transform([title, terms_list])
        df.iloc[i,:-1] = (tfidf * tfidf.T).A[0][:-1]
    df.sort_values(advisor, inplace=True, ascending=False)
    df = df.iloc[:limit,]
    df.to_csv(role + '_results.csv', index=False)

def add_and_retrain_model(model, data):
    pass

