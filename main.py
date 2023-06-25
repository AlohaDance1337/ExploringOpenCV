import cv2

img = cv2.imread('image_test.jpeg')
img = cv2.resize(img, (500,500))
print(img.shape)

cv2.imshow('Result', img)

cv2.waitKey(0)