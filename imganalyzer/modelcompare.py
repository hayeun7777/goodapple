# USAGE
# python test_nn.py --model gorb_apple.model --image examples/apple_new_01.png
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import cv2


imagePath = '../media/apple.png'

def analyze_picture(imagePath):
	# import the necessary packages and model
	# load the trained convolutional neural network
	model = load_model("gorb_apple.model")

	# construct the argument parse and parse the arguments
	# ap = argparse.ArgumentParser()
	# ap.add_argument("-m", "--model", required=True,
	# 	help="path to trained model")
	# ap.add_argument("-i", "--image", required=True,
	# 	help="path to input image")
	# args = vars(ap.parse_args())

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

	# Return Boolean instead of rating
	# if apple_good > 0.6:
	# 	return True
	# else:
	# 	return False

	# build the label

	# Option 2
	# label = "Good Apple Meter"
	# proba = apple_good
	# label = "{}: {:.2f}%".format(label, proba * 100)
	#
	# # draw the label on the image
	# output = imutils.resize(orig, width=400)
	# cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	# 	0.7, (0, 255, 0), 2)
	#
	# # show the output image
	# cv2.imshow("Output", output)
	# cv2.waitKey(0)


analyze_picture(imagePath)
