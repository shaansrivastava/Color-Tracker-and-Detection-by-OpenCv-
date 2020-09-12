# -*- coding: utf-8 -*-
import cv2
import numpy as np

def nothing(x):
    pass
cap=cv2.VideoCapture(0);
cv2.namedWindow('tracker')


cv2.createTrackbar('LH','tracker',0,255,nothing)
cv2.createTrackbar('LS','tracker',0,255,nothing)
cv2.createTrackbar('LV','tracker',0,255,nothing)
cv2.createTrackbar('UH','tracker',255,255,nothing)
cv2.createTrackbar('US','tracker',255,255,nothing)
cv2.createTrackbar('UV','tracker',255,255,nothing)

while(True):
    #frame=cv2.imread('smarties.png')
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lhue=cv2.getTrackbarPos('LH', 'tracker')
    hhue=cv2.getTrackbarPos('UH', 'tracker')
    lsat=cv2.getTrackbarPos('LS', 'tracker')
    hsat=cv2.getTrackbarPos('US', 'tracker')
    lval=cv2.getTrackbarPos('LV', 'tracker')
    hval=cv2.getTrackbarPos('UV', 'tracker')
    l_b=np.array([lhue,lsat,lval])
    u_b=np.array([hhue,hsat,hval])
    mask=cv2.inRange(hsv,l_b,u_b)
    
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()