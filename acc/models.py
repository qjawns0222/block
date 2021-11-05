from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings
# Create your models here.
class User(AbstractUser):
    comment = models.TextField()
    nickname = models.CharField(max_length=30)
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="usr/%y")
    follow=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def getpic(self):
        if self.pic:
            return self.pic.url
        else:
         return "/media/need.png"
    
    def summary(self):
        if len(self.content)>10:
            return self.content[:10]+"..."
        return self.content
class Follow(models.Model):
    follower = models.ManyToManyField(User,blank=True, related_name='follower')
    followee =models.ManyToManyField(User, blank=True , related_name='followee')  
    