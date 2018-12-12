from django.db import models

# Create your models here.
class Grades(models.Model):
    gname   =models.CharField(max_length=20)
    gdate   =models.DateTimeField()
    ggirlnum=models.IntegerField()
    gboynum =models.IntegerField()
    isdelete=models.BooleanField(default=False)
class Students(models.Model):
    sname   =models.CharField(max_length=20)
    sgender =models.BooleanField(default=True)
    sage    =models.IntegerField()
    scontend=models.CharField(max_length=20)
    isdelete=models.BooleanField(default=False)
    #关联外键
    sgrade=models.ForeignKey("Grades")