from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Question(models.Model):
    """
    Model for user to submit a question.
    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL
    )
    question = models.TextField(null=False, blank=False)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.question[:50]
