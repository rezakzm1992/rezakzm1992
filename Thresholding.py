import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#                   Simple ThreshHolding
#  first we get the binary and blurred image. set a Value of T. The values higher or
#  lesser than T becames what we define. T is set Manually.
def ThreshInv(image, x, k):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (k, k), 0)
    # cv2.imshow("blurredBnW", blurred)
    (T, threshinv) = cv2.threshold(blurred, x, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("threshedInv", threshinv)
    cv2.imshow("output threshInv", cv2.bitwise_and(image, image, mask=threshinv))
    cv2.waitKey(0)
    return threshinv
# z = int(input('enter T:'))
# k = int(input('inter Kernel:'))
# ThreshInv(image, z, k)

def Thresh(image, x, k):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (k, k), 0)
    # cv2.imshow("blurredBnW", blurred)
    (T, thresh) = cv2.threshold(blurred, x, 255, cv2.THRESH_BINARY)
    cv2.imshow("threshedInv", thresh)
    cv2.imshow("output thresh", cv2.bitwise_and(image, image, mask=thresh))
    cv2.waitKey(0)
    return thresh
# z = int(input('enter T:'))
# k = int(input('inter Kernel:'))
# Thresh(image, z, k)

#               Otsu ThreshHoling
#   in this method T is automatically calculated by assuming a bi-modal distribution
#   of grayscale pixel values and finding optimum point of seperator.
#   the 2nd arg of cv2.threshhold is 0.
def Otsu(image, k):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (k, k), 0)
    # cv2.imshow("blurredBnW", blurred)
    (T, threshOtsu) = cv2.threshold(blurred, 0, 255,
                                    cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("threshedInv", threshOtsu)
    cv2.imshow("output threshOTSU", cv2.bitwise_and(image, image, mask=threshOtsu))
    print(T)
    cv2.waitKey(0)
    return threshOtsu
# k = int(input('inter Kernel:'))
# Otsu(image,  k)


#                   Adaptive ThreshHolding
# adaptive thresh considers small neighbors of pixels and then finds
# an optimal threshold value T for each neighbor.
# this means we separate image to blocks
# our goal is to statistically (Arthmetic or Gaussian) examine the pixel
# intensity values in the neighborhood of a given pixel p.

def Adaptivethresh(image, k, B, C):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (k, k), 0)
    # cv2.imshow("blurredBnW", blurred)
    Adaptthresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C
                                        , cv2.THRESH_BINARY_INV, B, C)
    cv2.imshow("AdaptiveThresh", Adaptthresh)
    cv2.imshow("output AdaptiveThresh",
               cv2.bitwise_and(image, image, mask=Adaptthresh))
    cv2.waitKey(0)
    return Adaptthresh
# k = int(input('inter Kernel:'))
# B = int(input('input BlockSize:'))
# C = int(input('input Constant:'))
# Adaptivethresh(image, k, B, C)