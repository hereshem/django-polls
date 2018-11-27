from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField()

    def __str__(self):
        return self.title + " " + str(self.created)

class Choice(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title