from rest_framework import generics

from .api.serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset  = Article.objects.filter(visibility=True)

class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset  = Article.objects.all()
    lookup_field = 'slug'

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()

class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()