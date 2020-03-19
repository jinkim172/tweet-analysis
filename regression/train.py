import pandas
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import hstack
from sklearn.linear_model import Ridge

# file names
input_files_dir = 'input_files/'
training_objects_dir = 'training_objects/'
training_file = 'small_subset_train.csv'
model_file = 'small_subset_model.obj'
vectorizer_file = 'small_subset_vectorizer.obj'

print(f"Reading training data from {input_files_dir + training_file}...")
data = pandas.read_csv(input_files_dir + training_file, header=None, encoding='latin-1')

vectorizer = TfidfVectorizer(min_df=5)
x_train = vectorizer.fit_transform(data.iloc[:, 5].values)
x = hstack([x_train])
clf = Ridge()

y = data.iloc[:, 0].values
# fit model to the training data
print("Training linear regression model...")
clf.fit(x, y)

# save model and vectorizer
print(f"Saving model to {training_objects_dir + model_file} and vectorizer to {training_objects_dir + vectorizer_file}...")
with open(training_objects_dir + model_file, 'wb') as f:
    pickle.dump(clf, f)
with open(training_objects_dir + vectorizer_file, 'wb') as f:
    pickle.dump(vectorizer, f)
