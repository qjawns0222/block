from django.db import models
from acc.models  import User
# Create your models here.
class Gboard(models.Model):
    pic=models.ImageField(upload_to="gboard/%y/%m/%d")
    content=models.TextField()
    likey = models.ManyToManyField(User, blank=True)

class Hashtag(models.Model):
    hashtag = models.ManyToManyField(Gboard, blank=True)
    name= models.CharField(max_length=100)