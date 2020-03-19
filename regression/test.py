import pandas
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import hstack
from sklearn.linear_model import Ridge
from sklearn.metrics import explained_variance_score as evs

data = pandas.read_csv('small_subset_test.csv', header=None, encoding='latin-1')

with open('small_subset_vectorizer.obj', 'rb') as f:
    vectorizer = pickle.load(f)
with open('small_subset_model.obj', 'rb') as f:
    clf = pickle.load(f)

x_test = vectorizer.transform(data.iloc[:, 5].values)
x = hstack([x_test])

# predict on test data
results = clf.predict(x)

# for tweet, prediction, correct in zip(data.iloc[:, 5].values, results, data.iloc[:, 0].values):
#     print(tweet, "prediction:", prediction, ", correct:", correct)

print(evs(data.iloc[:, 0].values, results))