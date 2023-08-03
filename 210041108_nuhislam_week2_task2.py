import numpy as np
import cv2 as cv

def detect_red_and_white_regions(image):
    cv.imshow('Goat', img)
    #BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('HSV', hsv)
    lower_red_range = np.array([169, 100, 100])
    upper_red_range = np.array([189, 255, 255])
    lower_white_range = np.array([75, 0, 99])
    upper_white_range = np.array([179, 62, 255])

    masked_red = cv.inRange(hsv, lower_red_range, upper_red_range)
    masked_white = cv.inRange(hsv, lower_white_range, upper_white_range)
    mask = masked_white + masked_red
    cv.imshow('New', mask)
    cv.waitKey(0)

def analyze_goat(image_array):
    pix_max=np.amax(image_array)
    pix_min=np.amin(image_array)
    pix_avg=np.mean(image_array)
    pix_nonzero=np.count_nonzero(image_array)
    pix_zero=np.size(image_array)-np.count_nonzero(image_array)

    print("Minimum pixel :",pix_min)
    print("Maximum pixel :",pix_max)
    print("Average pixel :",pix_avg)
    print("Total nonzero  pixels :",pix_nonzero)
    print("Total zero  pixels :",pix_zero)




img = cv.imread('E:\OpenCV\photo\GOAT.jpg')
detect_red_and_white_regions(img)
gray= cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)
analyze_goat(gray)
