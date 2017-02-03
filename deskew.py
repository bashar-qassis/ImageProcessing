#!/usr/bin/env python
from cv2.cv2 import *

from skew_detect import *

from skimage import img_as_uint
from skimage.transform import rotate


class Deskew:
    def __init__(self, image, display_image, r_angle):

        self.image = image
        self.display_image = display_image
        self.r_angle = r_angle
        self.skewObj = Skew(self.image)

    def deskew(self):
        img=self.image
        res = self.skewObj.process_single_file(img)
        angle = res['Estimated Angle']

        if angle >= 0 and angle <= 90:
            rot_angle = angle - 90 + self.r_angle
        if angle >= -45 and angle < 0:
            rot_angle = angle - 90 + self.r_angle
        if angle >= -90 and angle < -45:
            rot_angle = 90 + angle + self.r_angle

        rotated = rotate(img, rot_angle, resize=True, cval=50)

        # if self.display_image:
        #     self.display(rotated)
        image = rotated*255
        _,image = threshold(image,150,255,THRESH_BINARY)
        return image

    # def saveImage(self, img):
    #     path = self.skewObj.check_path(self.output_file)
    #     io.imsave(path, img.astype(np.uint8))

    def display(self, img):

        plt.imshow(img)
        plt.show()

    def run(self):
        return (self.deskew()).astype(np.uint8)



if __name__ == '__main__':
    parser = optparse.OptionParser()

    parser.add_option('-i', '--input', default=None, dest='input_file', help='Input file name')
    parser.add_option('-d', '--display', default=None, dest='display_image', help="display the rotated image")
    parser.add_option('-r', '--rotate', default=0, dest='r_angle', help='Rotate the image to desired axis', type=int)
    options, args = parser.parse_args()
    deskew_obj = Deskew(options.input_file, options.display_image, options.r_angle)
    deskew_obj.run()