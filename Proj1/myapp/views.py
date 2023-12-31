from .models import promodel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer
from django.shortcuts import render
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
	queryset = promodel.objects.all()
	serializer = ProductSerializer
	permissions_classes = ['permissions.IsAuthentication']