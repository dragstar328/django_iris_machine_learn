from django.shortcuts import render, redirect, get_object_or_404
from .models import Iris
from .forms import IrisForm
from .classifier import IrisClassifier

# Create your views here.

def iris_list(request):
  iriss = Iris.objects.all().order_by('classified_date')
  return render(request, 'iris/iris_list.html', {'iriss': iriss})

def init_clf(request):
  IrisClassifier.delete_dump()
  return redirect('iris_list')

def iris_classify(request):
  if request.method == 'POST':
    form = IrisForm(request.POST)
    clf = IrisClassifier()

    #IrisClassifier.delete_dump()

    if form.is_valid():
      iris = form.save(commit=False)
      predict = clf.predict(iris)
      prob = predict[0]
      classified = predict[1]
      iris.set_classified({'classified': classified, 'probability': prob})
      form = IrisForm(instance=iris)
      clf_hash = hash(clf)
      print("FORM", form)
      print("HASH", clf_hash)

      if 'check' in request.POST:
        pass
      elif 'rem_ml' in request.POST:
        clf.delete_dump()
      elif 'save' in request.POST:
        iris.save_classify()
        return redirect('iris_list')
  else:
    form = IrisForm()

  return render(request, 'iris/iris_classify.html', {'form': form})

def iris_view(request, iris_id):
  iris = get_object_or_404(Iris, id=iris_id)
  return render(request, 'iris/iris_view.html', {'iris': iris})
