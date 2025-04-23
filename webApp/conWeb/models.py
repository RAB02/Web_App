from django.db import models


# Create your models here.
class signUp(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Tasks(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    task_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField()
