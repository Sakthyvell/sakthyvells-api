from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'category.Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='article'
    )
    body = RichTextUploadingField()
    cover_photo = models.ImageField(
        upload_to='blog/%Y/%m/%d', null=False, blank=False)
    visibility = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(max_length=255, unique=True, populate_from=('title',))

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-updated_on']

    def __str__(self) -> str:
        return self.title
