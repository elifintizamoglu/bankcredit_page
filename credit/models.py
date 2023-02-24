from django.db import models

# Create your models here.

class Credit(models.Model):
    name = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    interest_rate = models.DecimalField(max_digits=6,decimal_places=4)
    
