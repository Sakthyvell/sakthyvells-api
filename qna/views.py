from rest_framework import generics

from .api.serializers import QuestionSerializer
from .models import Answer, Question

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset  = Question.objects.all()

class QuestionDetailView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset  = Question.objects.all()
    lookup_field = 'slug'