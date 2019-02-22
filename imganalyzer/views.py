from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from materialize_nav import NavView


# Create your views here.
def index(request):
	return HttpResponse("Hello, world. Youre at goodapple!")
	
def home(request):
	if request.method == 'POST': 
		if request.FILES['photo']:
			uploaded_img = request.FILES['photo']
			fs = FileSystemStorage()
			fs.save(uploaded_img.name, uploaded_img)
			# return redirect(request, 'apple/result.html')
		else:
			print('bruh')
	return render(request, 'apple/home.html')

def result(request):
	return render(request, 'apple/result.html')

def details(request):
	return render(request, 'apple/details.html')

# Materialize navbar
def show_page(request):
	context = NavView.get_context(request, title="My Page")
	context["object"] = "MyObject"
	return render(request, "apple/home.html", context)