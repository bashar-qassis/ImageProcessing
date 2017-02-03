from time import sleep

from cv2.cv2 import *
import numpy as np
from matplotlib import pyplot as plt

from deskew import Deskew

path = "C:\\Users\\OmarMarridi\\Desktop\\Semester\\Digtal Image Processing\\ImageProject\\Preprocessing DataSet\\"
deskew_obj = Deskew(path+'Doc14.tif', 'Yes', 0)
image=deskew_obj.run()
image = threshold(image,130,255,THRESH_BINARY)
imwrite(path+'testborder.tif',image[1])