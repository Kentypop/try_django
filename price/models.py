from django.db import models
from django.contrib.auth.models import User

class PriceQuerySet(models.QuerySet):
	def maxtomin(self):
		#get_queryset() is = Price.objects
		return self.order_by('price')	
 

class PriceManager(models.Manager):
	def get_queryset(self):
		return PriceQuerySet(self.model, using=self._db)

	def maxtomin(self):
		return self.get_queryset().maxtomin()	

#class PriceManager(models.Manager):
#	def maxtomin(self):
#		#get_queryset() is = Price.objects
#		return self.get_queryset().all().order_by('price')

# Create your models here.
class Price(models.Model):
	name= models.CharField(max_length=50)
	price= models.DecimalField(max_digits= 5, decimal_places=2)
	author= models.ForeignKey(User, on_delete= models.CASCADE)

	objects= PriceManager()	

	def __str__(self):
		return self.name

