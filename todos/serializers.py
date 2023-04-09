from django.db.models import Count
from rest_framework import serializers
from .models import Todo
from django.db.models import F

class TodoSerializer(serializers.Serializer):
    text = serializers.CharField()
    completed = serializers.BooleanField(required=False)
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, required=False)
    last_updated = serializers.DateTimeField(read_only=True, required=False)
    order = serializers.IntegerField(required=True)

    class Meta:
        model = Todo
        fields = '__all__'
    
    def create(self, validated_data):
        in_todo = Todo(**validated_data)
        in_todo.save()
        return in_todo

    def update(self, instance, validated_data):
        instance.order = validated_data.get('order', instance.order)
        instance.text = validated_data.get('text', instance.text)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance