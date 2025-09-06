from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.IntegerField()
    password=models.CharField(max_length=250)
    confirm_password=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
