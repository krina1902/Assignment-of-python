from django.db import models

# Create your models here.

class Admin(models.Model):
	
	product_name=models.CharField(max_length=100)
	product_id=models.PositiveSmallIntegerField()
	

	def __str__ (self):
		return  self.product_name

class Productmanager(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveSmallIntegerField()
	address=models.TextField()
	password=models.CharField(max_length=100)

	def __str__(self):
		return self.fname