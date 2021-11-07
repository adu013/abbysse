# answers/models.py
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Answer(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL
    )
    question = models.ForeignKey(
        "questions.Question",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    answer = models.TextField(null=False, blank=False)
    anonymous = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer[:50]
