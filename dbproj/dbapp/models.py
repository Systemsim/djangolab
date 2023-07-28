from django.db import models

# Create your models here.
class Book(models.Model):
	bname= models.CharField(max_length=30)
	bauthor= models.CharField(max_length=30)
	bdesc= models.TextField()
	bprice= models.IntegerField(default=500)

	def __str__(self):
		return self.bname+" by "+self.bauthor
