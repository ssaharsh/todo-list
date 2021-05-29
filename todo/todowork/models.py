from django.db import models

# Create your models here.
class Task(models.Model):
    Title =  models.CharField(max_length=30)
    Desc = models.TextField()
    Time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

