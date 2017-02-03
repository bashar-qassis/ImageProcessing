from cv2.cv2 import *
import numpy
path = "C:\\Users\\OmarMarridi\\Desktop\\Semester\\Digtal Image Processing\\ImageProject\\Preprocessing DataSet\\"
#img = imread(path+'Magazine005.tif')
img = imread(path+'Doc14.tif')
gray = cvtColor(img,COLOR_BGR2GRAY)
_,thresh = threshold(gray,1,255,THRESH_BINARY)
contours = findContours(thresh,RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
cnt = contours[0]
x,y,w,h = boundingRect(cnt)
crop = img[y:y+h,x:x+w]
imwrite(path+'sofwinres.tif',crop)