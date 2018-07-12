from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=30)
    id=models.IntegerField(primary_key=True)
    email=models.EmailField()
class Course(models.Model):
    Cname=models.CharField(max_length=20)
    Duration=models.CharField(max_length=10)
    CId=models.ForeignKey(Student,on_delete=models.CASCADE)

