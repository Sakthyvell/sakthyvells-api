from rest_framework import generics

from .api.serializers import QuestionSerializer
from .models import Question

class QuestionListView(generics.ListAPIView):
    """QuestionListView
        Returns a list of questions
    """
    serializer_class = QuestionSerializer
    queryset  = Question.objects.all()

class QuestionDetailView(generics.RetrieveAPIView):
    """QuestionDetailView
        Returns a single question using slug as request
    """
    serializer_class = QuestionSerializer
    queryset  = Question.objects.all()
    lookup_field = 'slug'