from rest_framework import generics

from .api.serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset  = Article.objects.all()

class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset  = Article.objects.all()

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()

class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()