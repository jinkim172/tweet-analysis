# get sentiment for a line in stdin
import pandas
import pickle
from scipy.sparse import hstack
from sys import stdin

training_objects_dir = 'training_objects/'
model_file = 'small_subset_model.obj'
vectorizer_file = 'small_subset_vectorizer.obj'
DEBUG = False

if DEBUG:
    print(f"Loading model from {training_objects_dir + model_file} and vectorizer from {training_objects_dir + vectorizer_file}...")
with open(training_objects_dir + vectorizer_file, 'rb') as f:
    vectorizer = pickle.load(f)
with open(training_objects_dir + model_file, 'rb') as f:
    clf = pickle.load(f)

if DEBUG:
    print("Ready. Input tweets as lines in stdin...")
for line in stdin:
    line = pandas.DataFrame([line.strip()])
    x_test = vectorizer.transform(line.iloc[:, 0].values)
    x = hstack([x_test])

    # predict on test data
    [prediction] = clf.predict(x)
    print(prediction)