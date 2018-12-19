from django.db import models

# Create your models here.

class Videos(models.Model):
    title=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50)
    #img=models.ImageField(upload_to=,blank=True)
    hot=models.IntegerField(max_length=255)
    time=models.DateField()



