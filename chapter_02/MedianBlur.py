#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
file_full_path = "/home/tianyu/software/IDEAProjects/computer_vision_algorithm/lena.jpg"
image = cv2.imread(file_full_path)

#中值滤波
medianImage = cv2.medianBlur(image, 5)
cv2.imshow("Source Image", image)
cv2.imshow("median Image", medianImage)
cv2.waitKey()
cv2.destroyAllWindows()