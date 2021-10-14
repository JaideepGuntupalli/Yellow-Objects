import cv2 as cv
import numpy as np

def yellow_mask(hsv_img, light_yellow, dark_yellow):
    # Making a yellow mask
    yellow_mask = cv.inRange(hsv_img, light_yellow, dark_yellow)

    contours,hierarchies=cv.findContours(yellow_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    imp_contours=[]
    for i in contours:
        peri=cv.arcLength(i,True)
        if peri>29:
            imp_contours.append(i)

    blank=np.zeros(yellow_mask.shape,'uint8')

    final_mask=cv.drawContours(blank,imp_contours,-1,(255,255,255),-1)

    return final_mask,imp_contours