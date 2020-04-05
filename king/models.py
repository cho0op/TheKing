from django.db import models

class King(models.Model):
    name=models.CharField(max_length=20)
    picture=models.ImageField(upload_to='images')

# Create your models here.
