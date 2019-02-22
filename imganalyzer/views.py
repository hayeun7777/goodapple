from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. Youre at goodapple!")
	
def home(request):
	if request.method == 'POST' and request.FILES['photo']:
		uploaded_img = request.FILES['photo']
		fs = FileSystemStorage()
		fs.save(uploaded_img.name, uploaded_img)
	return render(request, 'apple/home.html')

def result(request):
	return render(request, 'apple/result.html')

def details(request):
	return render(request, 'apple/details.html')
