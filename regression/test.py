import pandas
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import hstack
from sklearn.linear_model import Ridge
from sklearn.metrics import explained_variance_score as evs

testing_file = 'small_subset_test.csv'
model_file = 'small_subset_model.obj'
vectorizer_file = 'small_subset_vectorizer.obj'

print(f"Reading testing data from {testing_file}...")
data = pandas.read_csv(testing_file, header=None, encoding='latin-1')

print(f"Loading model from {model_file} and vectorizer from {vectorizer_file}...")
with open(vectorizer_file, 'rb') as f:
    vectorizer = pickle.load(f)
with open(model_file, 'rb') as f:
    clf = pickle.load(f)

x_test = vectorizer.transform(data.iloc[:, 5].values)
x = hstack([x_test])

# predict on test data
print("Predicting test data...")
results = clf.predict(x)

# for tweet, prediction, correct in zip(data.iloc[:, 5].values, results, data.iloc[:, 0].values):
#     print(tweet, "prediction:", prediction, ", correct:", correct)

print("Explained variance score (1.0 is best):", evs(data.iloc[:, 0].values, results))