from django.test import TestCase
from .models import Answer, Question

class AnswerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Answer.objects.create()


class QuestionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Question.objects.create()