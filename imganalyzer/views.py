from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. Youre at goodapple!")
  
def home(request):
	# return HttpResponse("HI HI HI HIH I")
    return render(request, 'apple/home.html')

def result(request):
	return render(request, 'apple/result.html')

def details(request):
	return render(request, 'apple/details.html')