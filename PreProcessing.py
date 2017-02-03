from time import sleep

from cv2.cv2 import *
import numpy
import math
from detect_blur import *
from deskew import Deskew

path = "C:\\Users\\OmarMarridi\\Desktop\\Semester\\Digtal Image Processing\\ImageProject\\Preprocessing DataSet\\"
files = ["Doc07.tif", "Doc08.tif", "Doc09.tif", "Doc011.tif", "Doc11.tif", "Doc12.tif", "Doc13.tif", "Doc14.tif", "Doc15.tif", "Doc077.tif", "Fax001.tif", "Fax003.tif", "wordlist12.tif", "wordlist23.tif", "Document001.tif", "Doc066.tif"]

for i in range(0,files.__len__()-1,1):
    print("Processing Image \""+files[i]+"\"")
    orig = imread(path+files[i],IMREAD_GRAYSCALE)
    img = orig
    deskew_obj = Deskew(img,'Yes', 0)
    image = deskew_obj.run()
    image = equalizeHist(image)
    _,image = threshold(image,130,255,THRESH_BINARY)
    _,thresh = threshold(image,1,255,THRESH_BINARY)
    contours = findContours(image,RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x,y,w,h = boundingRect(cnt)
    image = image[y:y+h,x:x+w]

    #if(detectBlur(img, 100)):
        #print("Blurred Image")
    blur = medianBlur(image,3)
    for k in range(1, 5, 1):
        blur = medianBlur(blur,3)

    # kernel = numpy.ones((2,2), numpy.uint8)
    # res = erode(blur, kernel,dst=blur,iterations=2)

    # for i in range(3,31,2):
    # temp = adaptiveThreshold(blur, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY,15,11)
    _,temp = threshold(blur,200,255,THRESH_OTSU)
    # imwrite('/home/bashar/Desktop/Images for project/out2.jpg', blur2)
    # kernel = numpy.ones((2,2), numpy.uint8)
    # print(temp[1])
    # res = erode(temp[1], kernel,dst=res,iterations=1)
    # res = erode(temp[1], kernel,dst=res,iterations=1)
    # res2 = dilate(res,kernel,dst=res2,iterations=2)
        # res = numpy.hstack([res])

    try:
        res = numpy.hstack((orig,temp))
    except:
        res = temp
        pass
    imwrite(path+"Modified_"+files[i], res)
