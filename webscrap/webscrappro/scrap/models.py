from django.db import models
# Create your models here.
class Links(models.Model):
    adress=models.CharField(max_length=250,null=True,blank=True)
    stringname=models.CharField(max_length=250,null=True,blank=True)