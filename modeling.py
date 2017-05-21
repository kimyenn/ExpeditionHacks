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

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

# remove punctuation, lowercase
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

def calculate_cosine_similarity(doc1, doc2):
    vect = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = vect.fit_transform([doc1, doc2])
    return (tfidf * tfidf.T).A


def obtain_new_feeds():
	feeds = feedReader()

	labels = ['title', 'summary', 'link', 'published']
	df = pd.DataFrame.from_records(feeds, columns=labels)
	for role in roles:
	    df[role[0]] = 0

def build_MultinomialNB(df):
    ### code to build a NB model for each role to be run for only the first time

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

def load_model(model):
	pass

def retrain_model(model, data):
	pass

