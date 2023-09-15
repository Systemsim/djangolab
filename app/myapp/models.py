from django.db import models

# Create your models here.
class promodel(models.Model):
	pname=models.CharField(max_length=30)
	pbrand=models.CharField(max_length=30)
	pprice=models.IntegerField(default=50)
	pstock=models.CharField(max_length=30)
	
