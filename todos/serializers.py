from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.Serializer):
    text = serializers.EmailField()

    def create(self, validated_data):
        return Todo(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('text', instance.text)
        return instance