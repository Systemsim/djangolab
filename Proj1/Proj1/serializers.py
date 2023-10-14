from rest_framework import serializers
from .models import promodel

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=promodel 
		fields='__all__'