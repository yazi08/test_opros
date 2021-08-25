

from django.db import models

# Create your models here.
from django.utils import timezone


class Quiz(models.Model):


    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

    @staticmethod
    def get_active():

        today = timezone.now().date()
        active_quizzes = Quiz.objects.filter(start_date__gte=today)
        return active_quizzes

class Question(models.Model):


    question_types = (
        (1, 'ОТКРЫТЫЕ ВОПРОСЫ'),
        (2, 'ЗАКРЫТЫЕ ВОПРОСЫ'),

    )
    question_type = models.IntegerField( choices=question_types,null=True)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)


    def __str__(self):
        return self.question_text

class Choice(models.Model):


    question_id = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    choice_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.choice_text

class AnswerTracker(models.Model):


    customer = models.IntegerField(verbose_name=('customer_id'))
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True, null=True)
    answer_text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.customer} - {self.question_id} - {self.choice_id or self.answer_text}'