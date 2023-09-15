from django.shortcuts import render
from .models import promodel
# Create your views here.

def index(request):
	return render(request, 'index.html')
def add(request):
	return render(request, 'add.html')
def display(request):
	return render(request, 'display.html')
def saveproduct(request):
	pname=request.GET['pname']
	pbrand=request.GET['pbrand']
	pprice=request.GET['pprice']
	pstock=request.GET['pstock']
	p=promodel(pname=pname,pbrand=pbrand,pprice=pprice,pstock=pstock)
	p.save()
	data=promodel.objects.all()
	return render(request, 'display.html', {'data':data})
