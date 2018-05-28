from django.test import TestCase
from .models import Iris

# Create your tests here.

class IrisModeltests(TestCase):

  def test_setclassified(self):
    irs = Iris()
    irs.set_classified({'classified': 'setosa', 'probability': 0.98})
    self.assertEqual(irs.classified, 'setosa')
    self.assertEqual(irs.probability, 0.98)

