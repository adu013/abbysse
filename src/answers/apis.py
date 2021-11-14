# answers/apis.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Answer
from .serializers import AnswerSerilaizer


class AnswerViewSet(ModelViewSet):
    """
    A ModelViewSet for listing, retrieving and creating questions
    :param int question: Filtering of answers for that particular question
    """
    queryset = Answer.objects.all().order_by('pk')
    serializer_class = AnswerSerilaizer
    permissions_classes = [IsAuthenticated,]

    def get_queryset(self):
        query_params = self.request.query_params
        question_id = query_params.get("question", None)
        if question_id:
            self.queryset = self.queryset.filter(question_id=question_id)
        return self.queryset
