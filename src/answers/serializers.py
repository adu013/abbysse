# answers/serializers.py
from rest_framework.serializers import ModelSerializer

from .models import Answer


class AnswerSerilaizer(ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
