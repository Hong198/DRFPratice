from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)