import pandas
import pickle
from scipy.sparse import hstack
from sklearn.metrics import explained_variance_score as evs

input_files_dir = 'input_files/'
training_objects_dir = 'training_objects/'
testing_file = 'subset_test.csv'
model_file = 'full_subset_model.obj'
vectorizer_file = 'full_subset_vectorizer.obj'

print(f"Reading testing data from {input_files_dir + testing_file}...")
data = pandas.read_csv(input_files_dir + testing_file, header=None, encoding='latin-1')

print(f"Loading model from {training_objects_dir + model_file} and vectorizer from {training_objects_dir + vectorizer_file}...")
with open(training_objects_dir + vectorizer_file, 'rb') as f:
    vectorizer = pickle.load(f)
with open(training_objects_dir + model_file, 'rb') as f:
    clf = pickle.load(f)

x_test = vectorizer.transform(data.iloc[:, 5].values)
x = hstack([x_test])

# predict on test data
print("Predicting test data...")
results = clf.predict(x)

# for tweet, prediction, correct in zip(data.iloc[:, 5].values, results, data.iloc[:, 0].values):
#     print(tweet, "prediction:", prediction, ", correct:", correct)

print("Explained variance score (1.0 is best):", evs(data.iloc[:, 0].values, results))
