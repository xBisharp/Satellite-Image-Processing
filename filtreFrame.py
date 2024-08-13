import cv2 as cv
import numpy as np
import re
import os
from MakeImageList import *

def Canny(current_nr):
    src_list = MakeSourceList()
    
    current_nr = int(current_nr)
    
    img=cv.imread(src_list[current_nr-1])


    gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

    canny = cv.Canny(gray,125,175)

    cv.imshow("Edges",canny)




def Blur(current_nr):

    src_list = MakeSourceList()
    
    current_nr = int(current_nr)
    
    img=cv.imread(src_list[current_nr-1])


    gauss = cv.GaussianBlur(img,(7,7),0)

    cv.imshow("GaussianBlur",gauss)




def ColorSpace(current_nr):

    src_list = MakeSourceList()
    
    current_nr = int(current_nr)
    
    img=cv.imread(src_list[current_nr-1])

    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    cv.imshow("HSV",hsv)


def Erode(current_nr):
    src_list = MakeSourceList()
    
    current_nr = int(current_nr)
    
    img=cv.imread(src_list[current_nr-1])

    eroded = cv.erode(img,(3,3),iterations=1)

    cv.imshow("Eroded",eroded)


def LAB(current_nr):

    src_list = MakeSourceList()
    
    current_nr = int(current_nr)
    
    img=cv.imread(src_list[current_nr-1])

    bgr = cv.cvtColor(img,cv.COLOR_BGR2LAB)

    cv.imshow("LAB",bgr)


def BGRR(current_nr):
    src_list = MakeSourceList()
    
    current_nr = int(current_nr)
    
    img=cv.imread(src_list[current_nr-1])

    bgr = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    cv.imshow("BGR",bgr)