from django.db import models

# Create your models here.
class product(models.Model):

	name = models.CharField(max_length=256)
	brand = models.CharField(max_length=256)
	category = models.CharField(max_length=256)
	retail_price = models.CharField(max_length=256)
	selling_price = models.CharField(max_length=256)
	rating = models.IntegerField()
	arrival = models.DateField()
	image = models.CharField(max_length=400,default="")

	def __str__(self):
		return self.name

class customer(models.Model):

	name = models.CharField(max_length=256)
	phone = models.CharField(max_length=256)
	email = models.CharField(max_length=256,primary_key=True)
	password = models.CharField(max_length=256)
	join_data = models.DateField()

	def __str__(self):
		return self.name