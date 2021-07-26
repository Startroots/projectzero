from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Job(models.Model):
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=200)
    link_picture = models.CharField(max_length=200)