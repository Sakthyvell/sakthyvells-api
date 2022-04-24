from rest_framework import generics

from .api.serializers import AnswerSerializer, QuestionSerializer
from .models import Answer, Question


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    queryset  = Answer.objects.all()

class AnswerDetailView(generics.RetrieveAPIView):
    serializer_class = AnswerSerializer
    queryset  = Answer.objects.all()

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset  = Question.objects.all()

class QuestionDetailView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset  = Question.objects.all()