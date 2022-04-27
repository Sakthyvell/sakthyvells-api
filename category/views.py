from rest_framework import generics

from .api.serializers import CategorySerializer
from .models import Category

class CategoryListView(generics.ListAPIView):
    """CategoryListView
        Returns a list of categories
    """
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()