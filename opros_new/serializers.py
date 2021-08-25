
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']






class QuizSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Quiz
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type', 'choice_set']


class AnswerTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerTracker
        fields = '__all__'


class AnswerSerializer(serializers.Serializer):
    quiz = serializers.SerializerMethodField('get_quiz_title')
    question = serializers.SerializerMethodField('get_question_text')
    answer_text = serializers.CharField()
    choice = serializers.SerializerMethodField('get_choice_text')

    def get_quiz_title(self, obj):
        return obj.quiz_id.title

    def get_question_text(self, obj):
        return obj.question_id.question_text

    def get_choice_text(self, obj):
        return obj.choice_id.choice_text if obj.choice_id else None


class AnsweredQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerTracker
        fields = ['question_id', 'choice_id', 'answer_text']