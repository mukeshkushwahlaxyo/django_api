from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Vedio(models.Model):
	title = models.CharField(max_length = 80,null=True)
	description = models.TextField(max_length = 500,null=True)
	url = models.URLField()
	subcategory = models.TextField(max_length = 50,null=True)
	author = models.CharField(max_length = 50,null=True)

class Rating(models.Model):
	video = models.ForeignKey(Vedio,on_delete = models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	star = models.IntegerField()
	comments = models.TextField(max_length=300)