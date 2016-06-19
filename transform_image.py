from transform import four_point_transform
import numpy as np
import argparse
import cv2

# contruct + parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-b', '--base', help = 'base image to be overlayed')
ap.add_argument('-i', '--image', help = 'path to the image file')
ap.add_argument('-c', '--coords', help = 'comma seperated list of source points')
ap.add_argument('-o', '--output', help = 'output path')
args = vars(ap.parse_args())

# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread(args['image'])
base = cv2.imread(args['base'])
pts = np.array(eval(args['coords']), dtype = 'float32')

height = base.shape[0]
width = base.shape[1]

# resize the image so the transformation matches up
resized = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)

# apply the four point transform to obtain a birds eye view of the image
warped = four_point_transform(resized, height, width, pts)

cv2.imwrite(args['output'], warped)
