import cv2 as cv
from yellowFinder import *

def yellow_objects():
    #Taking image as an input from user
    img_address=input("Please Enter the address of the image : ")
    img = cv.imread(img_address)

    #appending the values returned by function to new variables
    yellow_object_img,yellow_objects_num = yellow_object_finder(img)


    print("Number of yellow objects in the given image are",yellow_objects_num)

    cv.imshow('Yellow objects',yellow_object_img)

    cv.waitKey(0)

if __name__=="__main__":
  yellow_objects()