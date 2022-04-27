from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

class Category(models.Model):
    """Category Model
    Store all categories
    Fields
        category: category name
        slug: slug of category
    """
    category = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=255, unique=True,
                         populate_from=('category',))

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category']

    def __str__(self) -> str:
        return self.category
