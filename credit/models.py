from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Credit(models.Model):
    name = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    slug = models.SlugField(default="",null=False,db_index=True)
    interest_rate = models.DecimalField(max_digits=6,decimal_places=4)
    loan_amount = models.IntegerField(default=500000,validators=[MinValueValidator(500000),MaxValueValidator(6000000)])

    def __str__(self):
        return f"{self.name}"
