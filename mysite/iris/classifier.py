from sklearn import svm, datasets, model_selection
from sklearn.externals import joblib
import os

fname = 'iris/svm_classifier.joblib'
classdict = {0: "setosa", 1: "versicolor", 2: "virginica"}


class IrisClassifier:

  def dump_classifier(self):
    iris = datasets.load_iris()
    clf = svm.SVC(probability=True)
    clf.fit(iris.data, iris.target)

    joblib.dump(clf, fname)
    print("DUMP!!")

  def predict(self, iris):
    if not os.path.exists(fname):
      self.dump_classifier()

    clf = joblib.load(fname)
    sl = iris.sepal_length
    sw = iris.sepal_width
    pl = iris.petal_length
    pw = iris.petal_width
    pre = clf.predict([[sl, sw, pl, pw]])
    prob = clf.predict_proba([[sl, sw, pl, pw]])

    return round(prob.max(), 4), classdict[pre[0]]

  @staticmethod
  def delete_dump():
    if os.path.exists(fname):
      os.remove(fname)
    print("DEL DUMP")
    return True
