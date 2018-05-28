from django import forms

from .models import Iris

class IrisForm(forms.ModelForm):
  classified = forms.CharField(required=False, disabled=True)
  probability = forms.FloatField(required=False, disabled=True)
  clf_hash = forms.IntegerField(required=False, disabled=True)

  class Meta:
    model = Iris
    fields = ('sepal_length',
              'sepal_width',
              'petal_length',
              'petal_width',
              'classified',
              'probability',
              'clf_hash'
             )

