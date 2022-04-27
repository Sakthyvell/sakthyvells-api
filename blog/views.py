from rest_framework import generics

from .api.serializers import ArticleSerializer
from .models import Article


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset  = Article.objects.filter(visibility=True)

class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset  = Article.objects.all()
    lookup_field = 'slug'