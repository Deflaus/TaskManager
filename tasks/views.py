from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskListSerializer, TaskCreateSerializer


class TasksListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user).order_by('-status').order_by('planned_completedtime')
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskCreateView(APIView):
    def post(self, request):
        task = TaskCreateSerializer(data=request.data)
        if task.is_valid():
            task.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)