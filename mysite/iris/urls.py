from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='iris_list'),
  path('iris_init_clf/', views.init_clf, name='init_clf'),
  path('classify/', views.iris_classify, name='iris_classify'),
  path('view/<int:pk>', views.DetailView.as_view(), name='iris_detail'),
  ]
