from multiprocessing.spawn import import_main_path
from django.urls import path, include
from .views import QuestionListView, QuestionDetailView


urlpatterns = [
    path('', QuestionListView.as_view()),
    path('<str:slug>', QuestionDetailView.as_view()),
]