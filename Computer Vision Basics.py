import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# M = np.float32([[1, 0, -50], [0, 1, -90]])
# shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#              Trasnslation
# def trans(image, x, y):
#     M = np.float32([[1, 0, x], [0, 1, y]])
#     shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#     return shifted
# shifted = trans(image, 10, 10)
# cv2.imshow("img", shifted)

#             Rotation
# def rotate(image, cX, cY, teta, sc):
#     M = cv2.getRotationMatrix2D((cX, cY), teta, sc)
#     rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#     return rotated
#
# rot = rotate(image, image.shape[1]//2, image.shape[0]//2, -45, 0.5)
# cv2.imshow("rot", rot)

#                Resize

# def resz(image, newwid):
#     r = newwid / image.shape[1]
#     dim = (newwid, int(image.shape[0]*r))
#     resz = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
#     return resz
# resized = resz(image, 1000)

# def resize(image, width=None, height=None, inter = cv2.INTER_AREA):
#     #We have also cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC and etc.
#     # dim = None
#     (h, w) = image.shape[:2]
#
#     if width is None and height is None:
#         return image
#     if height is None:
#         r = width / float(w)
#         dim = (width, int(h*r))
#
#     if width is None:
#         r = height / float(h)
#         dim = (int(w*r), height)
#
#     resize = cv2.resize(image, dim, interpolation=inter)
#     return resize
#
# resized = resize(image, height=100)
# cv2.imshow("resized", resized)

#         Flipping
# flipped = cv2.flip(image, -1) #0, 1, -1
# cv2.imshow("Org", image)
# cv2.imshow("flipped", flipped)

#         Cropping
# def crop(image, SH, EH, SW, EW):     #SH: S=Start, E=End, H=Height, W=Width
#     cropped = image[SH:EH, SW:EW]
#     return cropped
#
# crp = crop(image, 200, 350, 360, 490)
# cv2.imshow("crp", crp)

#           Image Arithmetic
#differnace between OpenCV & Numpy arithmetic

#   IN THIS MODE: CLIPPING
# print("cv add = {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
# print("cv subtract = {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
#
#IN THIS MODE: WRAPPING AROUND
# print("np add = {}".format(np.uint8([200]) + np.uint8([100])))
# print("np add = {}".format(np.uint8([50]) - np.uint8([100])))

# M = np.ones(image.shape, dtype="uint8") * 100
# added = cv2.add(image, M)
# sub = cv2.subtract(image, M)
# cv2.imshow("added", added)
# cv2.imshow("sub", sub)

#                  Bitwise Operation
# canvas1 = np.zeros((300, 300), dtype="uint8")
# rect = cv2.rectangle(canvas1, (25, 25), (275, 275), 255, -1)
# canvas2 = np.zeros((300, 300), dtype="uint8")
# circ = cv2.circle(canvas2, (150, 150), 150, 255, -1)
#
# AND = cv2.bitwise_and(rect, circ)
# OR = cv2.bitwise_or(rect, circ)
# XOR = cv2.bitwise_xor(rect, circ)
# NOT = cv2.bitwise_not(rect, circ)
# cv2.imshow("a", NOT)

#                   masking
# mask = np.zeros(image.shape[:2], dtype="uint8")
# # cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
# cv2.circle(mask, (145, 200), 120, 255, -1)
# # cv2.imshow("1", mask)
# masked = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow("masked", masked)

#               Split and Merge Channels
(B, G, R) = cv2.split(image)

# cv2.imshow("B", B)
# cv2.imshow("G", G)
# cv2.imshow("R", R)
merged = cv2.merge([B, G, R])
cv2.imshow("m", merged)

cv2.waitKey(0)
