from django.contrib import admin
from .models import Question, Answer


class AnswerAdmin(admin.ModelAdmin):
    autocomplete_fields = ["question"]

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)