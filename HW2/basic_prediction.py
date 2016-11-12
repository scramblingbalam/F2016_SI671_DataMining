from __future__ import division
import time
import csv
import numpy as np
import codecs
import unicodedata
from collections import Counter
from sklearn.svm import SVR
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer
from sklearn import svm
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class ItemSelector(BaseEstimator, TransformerMixin):
    """For data grouped by feature, select subset of data at a provided key.

    """
    def __init__(self, key):
        self.key = key

    def fit(self, x, y=None):
        return self

    def transform(self, data_dict):	
        return data_dict[self.key]


class filter_DF_Fields(BaseEstimator, TransformerMixin):
    """Extract features from each document for DictVectorizer"""

    def __init__(self, keys):
        self.keys = keys

    def fit(self, x, y=None):
        return self

    def transform(self, DF):
        return [{j:DF.loc[i,j] 
        		for j in DF.columns 
        		if j not in self.keys} 
        		for i in range(len(DF))]


# comma delimited is the default
train_df = pd.read_csv("train.csv", header = 0)
	# print unicodedata.normalize('NFC', unicode(i["Tweet"]))

train_header = ["Class","Pos_words","Neg_words","FoodPos_words","FoodNeg_words","FoodNeut_words","Alcohol_words","Tweet"]


# count_vect = CountVectorizer(decode_error='ignore')


text_clf = Pipeline([('selector', ItemSelector(key='Tweet')),
					('vect', CountVectorizer(decode_error='ignore')),
					('tfidf', TfidfTransformer())
					])


sentiment = Pipeline([('selector', filter_DF_Fields(keys= ["Class","Tweet","ID"] )),
					('vect', DictVectorizer())
					])

pipeline = Pipeline([
    ('feats', FeatureUnion([
        ('idf', text_clf), # can pass in either a pipeline
        ('sentiment', sentiment) # or a transformer
    ])),
    ('clf', svm.LinearSVC())  # classifier
])

('clf', MultinomialNB())

pipeline = pipeline.fit(train_df, train_df.Class)



test_header = ["ID","Pos_words","Neg_words","FoodPos_words","FoodNeg_words","FoodNeut_words","Alcohol_words","Tweet"]

test_df = pd.read_csv("test.csv", header = 0)
predicted = pipeline.predict(test_df)


output_df = pd.DataFrame.from_items([('ID', test_df.ID), ('Class', predicted)])

output_df.to_csv("output.csv",columns = ["ID","Class"])

print output_df

# for doc, category in zip(test_df.ID, predicted):
# 	print('%r => %s' % (doc, category))

# predClassCounter = Counter(predicted)
# print predClassCounter.most_common()

# classCounter = Counter(train_df.Class)
# print classCounter.most_common()


# print test_df

# print train_df.Tweet

# https://docs.python.org/2.4/lib/standard-encodings.html
# ascii
# cp037
# cp437
# cp500
# cp850
# cp1140
# latin_1
# iso8859_15
# mac_roman
# utf_16
# utf_8