from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from materialize_nav import NavView
from base64 import b64encode

# below are for the tensorflow model
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import cv2
import os
cwd = os.getcwd()


# Create your views here.
def index(request):
	return HttpResponse("Hello, world. Youre at goodapple!")

# tesnsor flow model
def analyze_picture(imagePath):
	# import the necessary packages and model
	# load the trained convolutional neural network
	model = load_model("imganalyzer/gorb_apple.model")

	# load the image
	image = cv2.imread(imagePath)
	orig = image.copy()
	
	# pre-process the image for classification
	image = cv2.resize(image, (28, 28))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	print('pass')
	# classify the input image
	# "apple_good" specifies the probability the apple is "good"
	# "apple_bad" specifies the probability the apple is "bad"
	(apple_bad, apple_good) = model.predict(image)[0]

	# rating scale (5* is best):
	## 0 - 0.20: *
	## 0.21 - 0.40: **
	## 0.41 - 0.60: ***
	## 0.61 - 0.80: ****
	## 0.81 - 1.00: *****

	if apple_good > 0.81:
		rating = 5
	elif apple_good > 0.61:
		rating = 4
	elif apple_good > 0.41:
		rating = 3
	elif apple_good > 0.21:
		rating = 2
	else:
		 rating = 1

	return rating
	# print(rating)

	
def home(request):
	if request.method == 'POST': 
		if request.FILES['photo']:
			uploaded_img = request.FILES['photo']
			# data = photo.read()
			# encoded = b64encode(data)
			# mime = "image/jpg"
			# mime = mime + ";" if mime else ";"
			# f = "data:%sbase64,%s" % (mime, encoded[2:-1])
			fs = FileSystemStorage()
			fs.save(uploaded_img.name, uploaded_img)
			uploadedPhoto = 'media/' + uploaded_img.name
			rating = analyze_picture(uploadedPhoto) # function for the comparison
			print(rating)
			# return redirect('imganalyzer:result', rating=4, img_string="hey")
			return render(request, 'apple/result.html', {'img_string': uploadedPhoto, 'rating': rating})
		else:
			print('bruh')
	return render(request, 'apple/home.html')

def details(request):
	return render(request, 'apple/details.html')