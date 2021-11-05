from django.db import models

# Create your models here.
class Trans(models.Model):
    text1 = models.CharField(max_length=100)
    
    text2 = models.CharField(max_length=100)