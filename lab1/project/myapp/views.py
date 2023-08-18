from django.shortcuts import render
from .models import Register 
# Create your views here.
def register(request):
	if request.method=='POST':
		fname=request.POST.get("fname")
		lname=request.POST.get("lname")
		email=request.POST.get("email")
		pswd=request.POST.get("pswd")
		cpswd=request.POST.get("cpswd")

		if pswd==cpswd:
			query=Register(fname=fname,lname=lname,email=email,pswd=pswd,cpswd=cpswd)
			query.save()
		else:
			pass
	return render(request,'signup.html')

def login(request):
	if request.method == "POST":
		fname=request.POST.get("fname")
		pswd=request.POST.get("pswd")

		checkuser=Register.objects.filter(fname=fname,pswd=pswd)
		if checkuser:
			request.session['fname']=fname
			return render(request, 'index.html' ,{'name':fname})


		else:
			pass
	return render(request,'login.html')

def index(request):
	return render(request,'index.html')