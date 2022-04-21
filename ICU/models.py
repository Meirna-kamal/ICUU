from django.db import models

# Create your models here.
class vitalSigns(models.Model):
    vitalSignsList=models.CharField(max_length=1000)