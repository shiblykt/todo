from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    status_choices = [('completed','COMPLETED'),('pending','PENDING')]
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    due = models.DateField()
    status = models.CharField(max_length=20,choices=status_choices,default='pending')


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['due']