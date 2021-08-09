import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#                Smooth Using Average Kernel
#     In this Method weight of the Kernel is equal
#        The larger the Kernel, The blurrer the Image :)
def Average(image, x):
    for i in range (1, x+1, 2):  #Kernel dimensions must be odd
        blurred = cv2.blur(image, (i, i))
        cv2.imshow("Blurred using Avg kernel {} x {}".format(i, i), blurred)
        cv2.waitKey(0)
    return blurred
# Average(image, 9)

#                Smooth Using Gaussian Kernel
#     In this Method weight of the Kernel is NOT equal and follows Gaussian formula
#        The larger the Kernel, The blurrer the Image :)
#     less blur than Averaging but more natural blurring in this method is being achieved
def Gaussian(image, x):
    for i in range (1, x+1, 2):  #Kernel dimensions must be odd
        blurred = cv2.GaussianBlur(image, (i, i), 0)
        cv2.imshow("Blurred using Gaussian kernel {} x {}".format(i, i), blurred)
        cv2.waitKey(0)
    return blurred
# Gaussian(image, 9)

#                Smooth Using Median Kernel
#     In this Method the median in the Kernel elements is computed then it's being put
#     to the center
#           This method is very effective in removing salt and pepper noise
def Median(image, x):
    for i in range (1, x+1, 2):  #Kernel dimensions must be odd
        blurred = cv2.medianBlur(image, i)
        cv2.imshow("Blurred using Median kernel {} x {}".format(i, i), blurred)
        cv2.waitKey(0)
    return blurred
# Median(image, 9)

#                Smooth Using Bilateral Kernel
#     In this Method the noise is removed and meanwhile edges maintain
#     because of considering two Gaussian functions (Spatial and Intensity)
# which results in: only pixels with similar intensity are included
# in the actual computation of  the blur
def Bilateral(image, diameter, sigmaColor, sigmaSpace):
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv2.imshow("bilateral blurred using: diameter: {}, sigmaColor: {}, "
               "sigmaSpace: {}".format(diameter, sigmaColor, sigmaSpace), blurred)
    cv2.waitKey(0)
    return blurred
# Bilateral(image, 11, 91, 59)
# Bilateral(image, 11, 21, 7)
