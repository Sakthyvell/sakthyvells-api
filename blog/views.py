from rest_framework import generics

from .api.serializers import ArticleSerializer
from .models import Article


class ArticleListView(generics.ListAPIView):
    """ArticleListView
        Returns a list of arctiles which are visible
    """
    serializer_class = ArticleSerializer
    queryset  = Article.objects.filter(visibility=True)

class ArticleDetailView(generics.RetrieveAPIView):
    """ArticleDetailView
        Returns a single article using slug as request
    """
    serializer_class = ArticleSerializer
    queryset  = Article.objects.all()
    lookup_field = 'slug'