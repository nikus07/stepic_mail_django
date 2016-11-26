from django.db import models

#User model
from django.contrib.auth.models import User

#Question model

class Question(models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now = True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)

#Answer model
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now = True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)