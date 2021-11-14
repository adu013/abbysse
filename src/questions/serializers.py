# questions/serializers.py
from rest_framework.serializers import ModelSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'user',
            'anonymous',
            'locked',
            'created_on',
            'updated_on',
        ]
