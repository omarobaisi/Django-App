from django.db import models

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=30)
    start = models.DateField()
    Duration = models.IntegerField()
    teacher = models.ForeignKey('teacher', on_delete=models.CASCADE)
    student = models.ManyToManyField('student', related_name='student')


class teacher(models.Model):
    name = models.CharField(max_length=30)
    photo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=30)

class student(models.Model):
    name = models.CharField(max_length=30)
    birth = models.DateField()
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=30)