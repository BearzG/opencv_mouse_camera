import cv2
import numpy

img = cv2.imread('./book.jpg')
(width, height) = (img.shape[1], img.shape[0])
resized = cv2.resize(img, (width // 3, height // 3), cv2.INTER_AREA)
print(resized.shape)

cv2.imshow('Image', resized)

data = []

def mouse_events(event, x, y, flags, parms):
    if (event == cv2.EVENT_LBUTTONDOWN):
        data.append([x, y])
        cv2.circle(resized, (x, y), 4, (0, 0, 255), thickness=-1)
        cv2.imshow('Image', resized)


cv2.setMouseCallback('Image', mouse_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(data)

[top_l, top_r, center] = data

p1 = numpy.float32([top_l, top_r, center])
p2 = numpy.float32([[0, 0], [400, 0], [200, 600]])

math = cv2.getAffineTransform(p1, p2)

affined = cv2.warpAffine(resized, math, (400, 600))

cv2.imshow("Final", affined)
cv2.imshow('Original', resized)
cv2.waitKey(0)
