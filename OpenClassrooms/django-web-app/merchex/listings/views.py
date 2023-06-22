from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from django.shortcuts import render 

# Create your views here.

def hello(request):
	bands = Band.objects.all()
	return render(request,'bands/hello.html',{'bands': bands})

def about(request):
	return HttpResponse("<h1>A propos </h1> <p> Nous adorons merch! </p>")
	
