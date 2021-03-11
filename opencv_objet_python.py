# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 01:03:46 2021

@author: sebas
"""

#afficher une image avec OpenCV
import cv2
img=cv2.imread ("6.jpg")
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#changement de couleur
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
cv2.imshow('hsv',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Transformer une image en niveau de gris

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.imshow('gray',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()