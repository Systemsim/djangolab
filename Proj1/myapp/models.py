from django.db import models

# Create your models here.
class promodel(models.Model):
	pname=models.CharField(max_length=20)
	price=models.CharField(max_length=20)

	def __str__(self):
		return self.pname