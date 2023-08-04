from django.db import models

# Create your models here.
class Pmanagment(models.Model):
	firstname= models.CharField(max_length=30)
	lastname= models.CharField(max_length=30)
	email= models.CharField(max_length=30)
	contactNo= models.IntegerField(default=10)
	
	def __str__(self):
		return self.firstname+" "+self.lastname
		