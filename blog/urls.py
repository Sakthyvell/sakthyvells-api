from multiprocessing.spawn import import_main_path
from django.urls import path, include
from .views import ArticleListView, ArticleDetailView, CategoryListView, CategoryDetailView


urlpatterns = [
    path("", ArticleListView.as_view()),
    path("category/", CategoryListView.as_view()),
    path("category/<int:pk>", CategoryDetailView.as_view()),
    path('<int:pk>', ArticleDetailView.as_view()),
]