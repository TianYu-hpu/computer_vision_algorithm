#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
file_full_path = "/home/tianyu/software/IDEAProjects/computer_vision_algorithm/lena.jpg"
image = cv2.imread(file_full_path)

#形态学滤波
cannyEdgeImage = cv2.Canny(image, 100, 200)
cv2.imshow("Source Image", image)
cv2.imshow("canny Image", cannyEdgeImage)
cv2.waitKey()
cv2.destroyAllWindows()