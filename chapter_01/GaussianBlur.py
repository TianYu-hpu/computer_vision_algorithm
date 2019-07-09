#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
file_full_path = "/home/tianyu/software/IDEAProjects/computer_vision_algorithm/lena.jpg"
image = cv2.imread(file_full_path)

#对图像做高斯平滑处理并显示
gaussianImage = cv2.GaussianBlur(image, (5, 5), 0)
#中值滤波
medianImage = cv2.medianBlur(image, 0)
#形态学滤波
morphologyExImage = cv2.morphologyEx(image, cv2.getStructuringElement(cv2))
cv2.imshow("Source Image", image)
cv2.imshow("Gauss Filtered  Image", gaussianImage)
cv2.imshow("median blue Image", medianImage)
cv2.waitKey()
cv2.destroyAllWindows()