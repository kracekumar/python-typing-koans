import datetime
from django.utils import timezone
from django.db import models
from django.db.models import QuerySet
from typing import Type


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # Annotate the return type
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @classmethod
    # Annotate the return type
    def questions_published_in(cls: Type[Question], year: int):
        return Question.objects.filter(pub_date__year=year)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# annotate the return type
def create_question(question_text: str):
    qs = Question(question_text=question_text, pub_date=timezone.now())
    qs.save()
    return qs


# Annotate the function
def create_choice(question, choice_text):
    return question.choice_set.create(choice_text=choice_text)
