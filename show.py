import cv2

def show_image(image):
    img = cv2.imread(image)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
