from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    put_date = models.DateTimeField('date published')  # 日期

    def __str__(self):
        return self.question_text

    def was_pulished_recently(self):
        return self.put_date >= timezone.now - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # 整数类型

    def __str__(self):
        return self.choice_text
