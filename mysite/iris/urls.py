from django.urls import path

from . import views

urlpatterns = [
  path('', views.iris_list, name='iris_list'),
  path('iris_init_clf/', views.init_clf, name='init_clf'),
  path('classify/', views.iris_classify, name='iris_classify'),
  path('view/<int:iris_id>', views.iris_view, name='iris_view'),
  ]
