from cv2 import *
# import the necessary packages
from cv2.cv2 import *
from imutils import paths
import argparse
import cv2


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return Laplacian(image, CV_64F).var()

# loop over the input images
def detectBlur(gray, threshold):
    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    # gray = cvtColor(image, COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"
    result = False

    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < threshold:
        text = "Blurry"
        result = True

    # show the image
    putText(gray, "{}: {:.2f}".format(text, fm), (10, 30),
                FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # imshow("Image", image)
    # key = waitKey(0)

    return result
