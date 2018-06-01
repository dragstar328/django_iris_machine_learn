from django.shortcuts import render, redirect, get_object_or_404
from .models import Iris
from .forms import IrisForm
from .classifier import IrisClassifier

from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
  template_name = 'iris/iris_list.html'
  context_object_name = 'iriss'

  def get_queryset(self):
    return Iris.objects.order_by('-id')

def init_clf(request):
  IrisClassifier.delete_dump()
  return redirect('iris_list')

def iris_classify(request):
  clf = IrisClassifier()

  if request.method == 'POST':
    form = IrisForm(request.POST)

    if form.is_valid():
      iris = form.save(commit=False)
      params = {'sepal_length':iris.sepal_length,
                'sepal_width' :iris.sepal_width,
                'petal_length':iris.petal_length,
                'petal_width' :iris.petal_width}

      predict = clf.predict(params)
      prob = predict[0]
      classified = predict[1]
      clf_hash = predict[2]
      iris.set_classified({'classified': classified, 'probability': prob, 'clf_hash': clf_hash})
      form = IrisForm(instance=iris)

      if 'check' in request.POST:
        pass
      elif 'save' in request.POST:
        iris.save_classify()
        return redirect('iris_list')
  else:
    clf_hash = clf.crc32()
    form = IrisForm(initial={'clf_hash': clf_hash})

  return render(request, 'iris/iris_classify.html', {'form': form})

class DetailView(generic.DetailView):
  model = Iris

  def get_context_data(self, **kwargs):
    return super().get_context_data(**kwargs)

