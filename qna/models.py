from django.db import models
from django_extensions.db.fields import AutoSlugField

from ckeditor_uploader.fields import RichTextUploadingField


class Question(models.Model):
    """Question Model
    Store all questions
    Fields
        title: Title of question (for naming purpose)
        created_at: created ISO Timestamp
        updated_at: updated ISO Timestamp
        content: Question HTML String
        category: pk of Category Model
        slug: slug of question
    """
    title = models.CharField(blank=False, null=False, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    category = models.ForeignKey(
        'category.Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='question'
    )
    slug = AutoSlugField(max_length=255, unique=True,
                         populate_from=('content',))
    def __str__(self):
        return self.title


class Answer(models.Model):
    """Answer Model
    Store all answers
    Fields
        created_at: created ISO Timestamp
        updated_at: updated ISO Timestamp
        body: Answer HTML String
        question: pk of Question Model referenced
        reference: URL to source material (if any)
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = RichTextUploadingField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="answer")
    reference = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.body
