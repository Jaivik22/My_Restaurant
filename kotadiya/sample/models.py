from django.db import models

# Create your models here.
class food_items(models.Model):

    name = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price= models.CharField(max_length=50)