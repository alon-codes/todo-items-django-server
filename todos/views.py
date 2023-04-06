from django.shortcuts import render
from rest_framework import viewsets

from todos.models import Todo
from todos.serializers import TodoSerializer

# Create your views here.
class TodosViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
