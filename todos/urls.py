from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodosViewSet.as_view({ 'get': 'list', 'post': 'create', 'put': 'update'}), name='index'),
]