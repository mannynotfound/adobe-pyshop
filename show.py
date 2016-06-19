import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', help = 'image to sho')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('Image', img)
cv2.waitKey(0)
