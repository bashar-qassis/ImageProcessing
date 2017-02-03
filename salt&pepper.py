from cv2.cv2 import *
import numpy
path = "C:\\Users\\OmarMarridi\\Desktop\\Semester\\Digtal Image Processing\\ImageProject\\Preprocessing DataSet\\"
img = imread(path+'Fax001.tif')
gray = cvtColor(img,COLOR_BGR2GRAY)
for i in range(1, 80, 1):
    img= medianBlur(img,3)

imwrite(path+'sofwinres.tif',img)