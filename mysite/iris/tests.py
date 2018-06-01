from django.test import TestCase
from .models import Iris
from django.urls import reverse
from .classifier import IrisClassifier
from django.utils import timezone

# Create your tests here.

class IrisModeltests(TestCase):

  def test_setclassified(self):
    irs = Iris()
    irs.set_classified({'classified': 'setosa', 'probability': 0.98, 'clf_hash': 12345})
    self.assertEqual(irs.classified, 'setosa')
    self.assertEqual(irs.probability, 0.98)
    self.assertEqual(irs.clf_hash, 12345)

  def test_save_classify(self):
    irs = Iris(sepal_length=10,
               sepal_width =10,
               petal_length=10,
               petal_width =10
               )
    irs.save_classify()
    self.assertEqual(10, irs.sepal_length)
    self.assertIsNotNone(irs.classified_date)

def add_db_iris(params):
  sl = params['prop'][0]
  sw = params['prop'][1]
  pl = params['prop'][2]
  pw = params['prop'][3]

  return Iris.objects.create(sepal_length=sl, sepal_width=sw, petal_length=pl, petal_width=pw)

class IndexViewTests(TestCase):

  def test_no_iris(self):
    res = self.client.get(reverse('iris_list'))
    self.assertEqual(res.status_code, 200)
    self.assertQuerysetEqual(res.context['iriss'], [])

  def test_one_iris(self):
    add_db_iris({'prop': [10,10,10,10]})
    res = self.client.get(reverse('iris_list'))
    self.assertEqual(len(res.context['iriss']), 1)

class DetailViewTests(TestCase):

  def test1(self):
    pass


class ClassifyViewTests(TestCase):

  def test_clasifier(self):
    iris = {'sepal_length':10,
            'sepal_width' :10,
            'petal_length':10,
            'petal_width' :10}
    clf = IrisClassifier()
    predict = clf.predict(iris)
    self.assertIsNotNone(predict[0])
    self.assertIsNotNone(predict[1])
    self.assertIsNotNone(predict[2])
