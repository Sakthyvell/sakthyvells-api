from multiprocessing.spawn import import_main_path
from django.urls import path, include
from .views import AnswerListView, AnswerDetailView, QuestionListView, QuestionDetailView


urlpatterns = [
    path('answers/', AnswerListView.as_view()),
    path('answers/<int:pk>', AnswerDetailView.as_view()),
    path('questions/', QuestionListView.as_view()),
    path('questions/<int:pk>', QuestionDetailView.as_view()),
]