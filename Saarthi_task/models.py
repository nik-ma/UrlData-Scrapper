from django.db import models

# Create your models here.
class urlData(models.Model):
    inUrl=models.CharField(max_length=120)
    urlResponse=models.CharField(max_length=2000)
    
