from rest_framework import serializers
from .models import Task


class TaskListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created = serializers.DateTimeField()
    status = serializers.CharField(max_length=15)
    planned_completedtime = serializers.DateField()


class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    status = serializers.CharField(max_length=15)
    planned_completedtime = serializers.DateField()

    def create(self, validated_data):
        task = Task.objects.update_or_create(
            user = validated_data.get('user', None),
            defaults = {
                'title': validated_data.get('title'),
                'description': validated_data.get('description'),
                'status': validated_data.get('status'),
                'planned_completedtime': validated_data.get('planned_completedtime'),
            }
        )
        return task