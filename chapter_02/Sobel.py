#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

file_full_path = "/home/tianyu/software/IdeaProject/computer_vision_algorithm/lena.jpg"
image = cv2.imread(file_full_path)

#Sobel算子
#设置核
kernel = np.ones((5, 5), np.uint8)
sobelEdgeXImage = cv2.Sobel(image, cv2.CV_16S, 1, 0)
sobelEdgeYImage = cv2.Sobel(image, cv2.CV_16S, 0, 1)

#转回uint8
absX = cv2.convertScaleAbs(sobelEdgeXImage)
absY = cv2.convertScaleAbs(sobelEdgeYImage)


dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
cv2.imshow("Source Image", image)
cv2.imshow("sobelEdge X Image", absX)
cv2.imshow("sobelEdge Y Image", absY)
cv2.imshow("Result Image", dst)
cv2.waitKey()
cv2.destroyAllWindows()