import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#           Erosion

def erode(image, x):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range (0, 4):
        eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
        cv2.imshow("erd {} times".format(i + 1), eroded)

        cv2.waitKey(0)
    return eroded
# erode(image, 3)

#                Dilation

def dilate(image, x):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range (0, 4):
        dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
        cv2.imshow("erd {} times".format(i + 1), dilated)

        cv2.waitKey(0)
    return dilated

# dilate(image, 3)

#                Opening

def opening(image, x):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range (1, x+1):
       kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (i, i))
       # We have also cv2.MORPH_CORSS & ELIPCE...
       opened = cv2.morphologyEx(gray.copy(), cv2.MORPH_OPEN, kernel)
       cv2.imshow("Opening {} x {}".format(i, i), opened)

       cv2.waitKey(0)
    return opened
# opening(image, 7)

#                  CLOSING
def closing(image, x):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range (1, x+1):
       kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (i, i))
       # We have also cv2.MORPH_CORSS & ELIPCE...
       closed = cv2.morphologyEx(gray.copy(), cv2.MORPH_CLOSE, kernel)
       cv2.imshow("Closing {} x {}".format(i, i), closed)

       cv2.waitKey(0)
    return closed
# closing(image, 7)

#               Morphological Gradient
# (Differance between Dilation and Erosion; useful for extracting outline of an image
def morfgrad(image, x):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range (1, x+1):
       kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (i, i))
       # We have also cv2.MORPH_CORSS & ELIPCE...
       mgraded = cv2.morphologyEx(gray.copy(), cv2.MORPH_GRADIENT, kernel)
       cv2.imshow("Graded {} x {}".format(i, i), mgraded)

       cv2.waitKey(0)
    return mgraded
# morfgrad(image, 7)

#                       Top Hat/White Hat
#  means the Differance between the originl img (grayscale) and Opening
# is used to show Bright regions of an image on dark backgrounds.
def Whitehat(image, x, y):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x, y))

    TopHat = cv2.morphologyEx(gray.copy(), cv2.MORPH_TOPHAT, rectKernel)
    cv2.imshow("TopHat", TopHat)
    cv2.waitKey(0)
    return TopHat
# Whitehat(image, 13, 5)
# 13 and 5 are almost ratio of the car plate. in this way the result becomes good
# the x and y depends on application

def BlackHat(image, x, y):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x, y))

    BlackHat = cv2.morphologyEx(gray.copy(), cv2.MORPH_BLACKHAT, rectKernel)
    cv2.imshow("BlackHatHat", BlackHat)
    cv2.waitKey(0)
    return BlackHat
# BlackHat(image, 13, 5)
