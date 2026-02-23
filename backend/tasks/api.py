from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action 
from rest_framework.response import Response 

from .models import Task
from .serializers import TaskSerializer

# ✅ Todo en singular
from tasks.application.use_cases import ToggleTaskDoneUseCase
from tasks.infrastructure.django_repository import DjangoTaskRepository

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        repo = DjangoTaskRepository()
        use_case = ToggleTaskDoneUseCase(repo)
        
        try:
            task = use_case.execute(pk)
            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)