from django.db import models
from django.utils import timezone

import os
from .classifier import IrisClassifier
from sklearn.externals import joblib

# Create your models here.
class Iris(models.Model):
  sepal_length = models.FloatField()
  sepal_width = models.FloatField()
  petal_length = models.FloatField()
  petal_width = models.FloatField()
  classified = models.CharField(max_length=50, blank=True, null=True)
  classified_date = models.DateField(blank=True, null=True)
  probability = models.FloatField(blank=True, null=True)
  clf_hash = models.IntegerField(blank=True, null=True)

  def set_classified(self, result):
    self.classified = result['classified']
    self.probability = result['probability']
    self.clf_hash = result['clf_hash']

  def save_classify(self):
    self.classified_date = timezone.now()
    self.save()
