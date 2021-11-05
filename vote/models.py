from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

from acc.models import User
# Create your models here.
class Topic(models.Model):
    subject=models.CharField(max_length=100)
    writer=models.CharField(max_length=100)
    voter=models.ManyToManyField(User,blank=True)
    ctime=models.DateTimeField()
    content=models.TextField()

class Choice(models.Model):
    subject=models.ForeignKey(Topic, on_delete=models.CASCADE)
    select = models.CharField(max_length=100)
    comment=models.TextField()
    voter=models.ManyToManyField(User,blank=True)
    pic=models.ImageField(upload_to="vote/%y")

class Reply(models.Model):
    sub = models.ForeignKey(Topic, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=50)
    comment = models.TextField()
    pic=models.ImageField(upload_to="vote/%y")

    def getpic(self):
        if self.pic:
            return self.pic.url
        else:
            return "/media/need.png"