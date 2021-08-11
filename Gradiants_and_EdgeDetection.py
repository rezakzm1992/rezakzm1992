import argparse
import cv2
import numpy as np
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#                      Image Gradiant
#  it means a Directional change in image Intensity
#  a Gradiant measures the changes in pixel Intensity in the given Direction
#  by means of this, we are able to detect Edges through estimating
#    direction (orientation) together with magnitude
#  Magnitude is how strong is the Intensity Change
#  Direction is the DIrection of Intensity Change

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def ImgGradiant(image):
    gX = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx= 1, dy= 0)
    gY = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx= 0, dy= 1)

    # gX = cv2.Scharr(gray, ddepth=cv2.CV_64F, dx= 1, dy= 0)
    # gY = cv2.Sharr(gray, ddepth=cv2.CV_64F, dx= 0, dy= 1)

    gX = cv2.convertScaleAbs(gX)
    gY = cv2.convertScaleAbs(gY)

    SobelCombined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)
    cv2.imshow("gX", gX)
    cv2.imshow("gY", gY)
    cv2.imshow("gX & gY", SobelCombined)
    cv2.waitKey(0)
    return SobelCombined
# ImgGradiant(image)


#                 Canny Edge Detector
# EDGE: is de ned as discontinuities in pixel intensity, or more simply, a sharp
#       difference and change in pixel values.

def Cannny(image, Tlower, Tupper):
    blurred = cv2.GaussianBlur(gray.copy(), (5,5), 0)
    edged = cv2.Canny(blurred, Tlower, Tupper)
    cv2.imshow("edged", edged)
    cv2.waitKey(0)
    return edged
# Tlower = int(input('T Lower:'))
# Tupper = int(input('T Upper:'))
# Cannny(image, Tlower, Tupper)

#        Let's Find Tlower and TUpper Automatically

def auto_Canny(image, sigma = 0.001):
    blurred = cv2.GaussianBlur(gray.copy(), (5,5), 0)
    v = np.median(blurred)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    autoedged = cv2.Canny(blurred, lower, upper)
    cv2.imshow("autoedged", autoedged)
    cv2.waitKey(0)
    return autoedged
# sigma = float(input('Enter Sigma:'))
# auto_Canny(image)

#  Imutils also has developed a function for autoCanny:
# blurred = cv2.GaussianBlur(gray.copy(), (5,5), 0)
# IMUautoCanny = imutils.auto_canny(blurred, 0.33)
# cv2.imshow("Imutils AutoCanny", IMUautoCanny)
# cv2.waitKey(0)
