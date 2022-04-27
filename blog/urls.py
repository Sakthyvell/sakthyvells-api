from multiprocessing.spawn import import_main_path
from django.urls import path, include
from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    path("", ArticleListView.as_view()),
    path('<str:slug>', ArticleDetailView.as_view()),
]