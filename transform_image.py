from transform import four_point_transform
import numpy as np
import argparse
import cv2

def map_perspective(base, image, coords, output):
    # load the image and grab the source coordinates (i.e. the list of
    # of (x, y) points)
    # NOTE: using the 'eval' function is bad form, but for this example
    # let's just roll with it -- in future posts I'll show you how to
    # automatically determine the coordinates without pre-supplying them
    image = cv2.imread(image)
    base = cv2.imread(base)
    pts = np.array(eval(coords), dtype = 'float32')

    height = base.shape[0]
    width = base.shape[1]

    # resize the image so the transformation matches up
    resized = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)

    # apply the four point transform to obtain a birds eye view of the image
    warped = four_point_transform(resized, height, width, pts)

    cv2.imwrite(output, warped)
