from django.db import models
from django_extensions.db.fields import AutoSlugField

from ckeditor_uploader.fields import RichTextUploadingField


class Question(models.Model):
    title = models.CharField(blank=False, null=False, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    slug = AutoSlugField(max_length=255, unique=True,
                         populate_from=('content',))
    def __str__(self):
        return self.title


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
