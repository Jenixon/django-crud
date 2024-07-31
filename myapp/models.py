from django.db import models
class employee(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Job=models.CharField(max_length=100)
    Salary=models.IntegerField()

# Create your models here.
