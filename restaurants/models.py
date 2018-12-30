from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	reference = models.FileField(null=True, blank=True)
	logo = models.ImageField(null=True, blank=True)
	owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'assets')
	

	def __str__(self):
		return self.name


class Item (models.Model):
	name = models.CharField(max_length = 120)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField()
	restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name= 'items')

	def __str__(self):
		return self.name


# class RestaurantItems(models.Model):
# 	item = models.CharField(max_length=120)
# 	restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)