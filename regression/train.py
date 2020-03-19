import pandas
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import hstack
from sklearn.linear_model import Ridge

data = pandas.read_csv('small_subset_train.csv', header=None, encoding='latin-1')

vectorizer = TfidfVectorizer(min_df=5)

print(len(data.columns))
x_train = vectorizer.fit_transform(data.iloc[:, 5].values)
x = hstack([x_train])
clf = Ridge()

y = data.iloc[:, 0].values
# fit model to the training data
clf.fit(x, y)

# save model and vectorizer
with open('small_subset_model.obj', 'wb') as f:
    pickle.dump(clf, f)
with open('small_subset_vectorizer.obj', 'wb') as f:
    pickle.dump(vectorizer, f)
