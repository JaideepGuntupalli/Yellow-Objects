import cv2 as cv
import numpy as np
from yellowMask import yellow_mask

#Defing function to find yellow objects
def yellow_object_finder(image):
    # Converting given image to HSV
    hsv_img = cv.cvtColor(image, cv.COLOR_RGB2HSV)
        
    # Setting yellow range
    light_yellow = (84,73,79)
    dark_yellow  =(104,255,255)

    final_mask, imp_contours = yellow_mask(hsv_img, light_yellow, dark_yellow) 
    
    #Extraxting the yellow objects
    resulting_img = cv.bitwise_and(image, image, mask=final_mask)
    
    #finding total no. of yellow objects
    no_of_yellow_objects=len(imp_contours)
    
    return resulting_img, no_of_yellow_objects