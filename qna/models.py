from unicodedata import category
from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField

from blog.models import Category

from ckeditor_uploader.fields import RichTextUploadingField

class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    slug = AutoSlugField(max_length=255, unique=True, populate_from=('content',))
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="questions")

    def __str__(self):
        return self.content


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = RichTextUploadingField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="question")
    reference = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.body
