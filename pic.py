import random
import numpy as np
import cv2

def random_string():
	str_digits = '0123456789'
	str_lowercase= 'abcdefghijklmnopqrstuvwxyz'
	str_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	str_all = str_digits +  str_lowercase + str_uppercase

	string = random.sample(str_all,5)

	randomstring = ''.join(string)

	return randomstring
	

img = cv2.imread('RandomGray.png')

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,random_string(),(100,100), font, 1,(0,0,255),2)
cv2.imwrite('image1.jpg', img)
