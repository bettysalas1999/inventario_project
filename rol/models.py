from django.db import models

# Create your models here.
class Rol(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()