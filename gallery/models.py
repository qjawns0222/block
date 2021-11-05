from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import FileField

from acc.models import User

# Create your models here.
class Gallery(models.Model):
    key= models.ForeignKey(User,on_delete=models.CASCADE)
    subject= CharField(max_length=100)
    content=TextField()
    pic=models.FileField(blank=True, null=True)
    writer=CharField(max_length=100)
    def getpic(self):
        if self.pic:
            return self.pic.url
        else:
            return "/media/need.png"
   
    def summary(self):
            if len(self.content)>30:
                return self.content[:30]+"..."
            return self.content
from .models import Gallery
class Reply(models.Model):
    subject=models.ForeignKey(Gallery, on_delete=models.CASCADE)
    replyer=models.CharField(max_length=100)
    comment=models.TextField()
    pic=models.FileField(blank=True, null=True)

    def __str__(self):
        return self.replyer
    
    def getpic(self):
        if self.pic:
            return self.pic.url
        else:
            return "/media/need.png"

