from rest_framework import serializers
from qna.models import Question

import json
from django.core.serializers.json import DjangoJSONEncoder


class QuestionSerializer(serializers.ModelSerializer):
    """QuestionSerializer
        Serializer for Question Model
    """
    answers = serializers.SerializerMethodField('get_answers')
    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, question):
        answers = list(Answer.objects.filter(question=question).values('body', 'reference'))
        serialized_q = json.dumps(list(answers), cls=DjangoJSONEncoder)
        return serialized_q