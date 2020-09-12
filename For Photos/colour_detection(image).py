# -*- coding: utf-8 -*-
import cv2
import numpy
def nothing(x):
    pass

cv2.namedWindow('trackbar')

cv2.createTrackbar('LH','trackbar',0,255,nothing)
cv2.createTrackbar('LS','trackbar',0,255,nothing)
cv2.createTrackbar('LV','trackbar',0,255,nothing)
cv2.createTrackbar('UH','trackbar',255,255,nothing)
cv2.createTrackbar('US','trackbar',255,255,nothing)
cv2.createTrackbar('UV','trackbar',255,255,nothing)





while(True):
    img=cv2.imread('colors1.jpg')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos('LH','trackbar')
    l_s=cv2.getTrackbarPos('LS','trackbar')
    l_v=cv2.getTrackbarPos('LV','trackbar')
    h_h=cv2.getTrackbarPos('UH','trackbar')
    h_s=cv2.getTrackbarPos('US','trackbar')
    h_v=cv2.getTrackbarPos('UV','trackbar')
    l_b=numpy.array([l_h,l_s,l_v])
    u_b=numpy.array([h_h,h_s,h_v])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow('myimage',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1)==27:
        break
    
cv2.destroyAllWindows()
    
    
    
