#! /bin/env python3

import random
from time import sleep
import cv2


#image = cv2.imread('B01.png')
#cv2.imshow("OpenCV Image",image)
#cv2.waitKey(0)	

"""  
test = Image.open('B01.png')
sleep(10)
test.close()
"""

  
# open method used to open different extension image file
num=random.randint(1, 23)
if num>=10:
	im = cv2.imread(f'./F{num}.png') 
	cv2.imshow("F",im)
	cv2.waitKey(0)	
	cv2.destroyWindow("F")

else:
	im = cv2.imread(f'./F0{num}.png') 
	cv2.imshow("F",im)
	cv2.waitKey(0)	
	cv2.destroyWindow("F")


inp=input("Retro:[y/n]\n")
if inp=='y':

	if num>=10:
		im1 = cv2.imread(f'./B{num}.png') 
		cv2.imshow("F",im1)
		cv2.waitKey(0)	
		cv2.destroyWindow("F")
	else:
		im1 = cv2.imread(f'./B0{num}.png') 
		cv2.imshow("F",im1)
		cv2.waitKey(0)	
		cv2.destroyWindow("F")		

	
#if inp=='n':
	
