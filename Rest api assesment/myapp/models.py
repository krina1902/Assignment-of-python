from django.db import models

# Create your models here.

class Novel(models.Model):
	title=models.CharField(max_length=100,blank=True)
	content=models.CharField(max_length=100,blank=True)
	created_at=models.DateTimeField(null = True)
	updated_at=models.DateTimeField(null = True)

	def __str__(self):
		return self.title