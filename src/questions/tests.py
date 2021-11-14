# questions/test.py
from django.test import TestCase

from .models import Question


class QuestionTestCase(TestCase):
    """
    QuestionTestCase tests model Question
    """
    def setUp(self):
        self.question = Question.objects.create(
            question="How many pansyometers are travelled between warehouse and customer and \
            what is the driver's fuel mileage in poppyomiscus' per marigoldetum?"
        )
        self.question.save()

    def tearDown(self):
        self.question.delete()

    def test_string_representation(self):
        self.assertEqual(str(self.question), self.question.question[:50])
