from sklearn import svm, datasets, model_selection
from sklearn.externals import joblib
import binascii
import os

fname = 'iris/svm_classifier.joblib'
classdict = {0: "setosa", 1: "versicolor", 2: "virginica"}


class IrisClassifier:

  def dump_classifier(self):
    iris = datasets.load_iris()
    clf = svm.SVC(probability=True)
    clf.fit(iris.data, iris.target)

    joblib.dump(clf, fname)

  def predict(self, iris):
    if not os.path.exists(fname):
      self.dump_classifier()

    clf = joblib.load(fname)
    sl = iris['sepal_length']
    sw = iris['sepal_width']
    pl = iris['petal_length']
    pw = iris['petal_width']
    pre = clf.predict([[sl, sw, pl, pw]])
    prob = clf.predict_proba([[sl, sw, pl, pw]])

    return round(prob.max(), 4), classdict[pre[0]], self.crc32()

  def crc32(self):
    if not os.path.exists(fname):
      self.dump_classifier()

    with open(fname, 'rb') as f:
      checksum = binascii.crc32(f.read()) & 0xFFFFFFFF
    return checksum

  @staticmethod
  def delete_dump():
    if os.path.exists(fname):
      os.remove(fname)
    print("DEL DUMP")
    return True
