# questions/apis.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import get_object_or_404

from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    """
    A ModelViewSet for listing, retrieving and creating questions
    """
    queryset = Question.objects.all().order_by('pk')
    serializer_class = QuestionSerializer
    permissions_classes = [IsAuthenticated,]
