from django.db import models

class Todo(models.Model):
    task=models.CharField(max_length=120)
    completed=models.BooleanField(default=False)
