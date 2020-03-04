from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media',blank=True)
    post = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    #DateField('Career_Date')
    #IntegerField(default=0)
    #ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
    	return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Question(models.Model):
    question_text = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    def __str__(self):
        return self.choice_text