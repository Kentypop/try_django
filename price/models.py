from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Price(models.Model):
	name= models.CharField(max_length=50)
	price= models.DecimalField(max_digits= 5, decimal_places=2)
	author= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.name