#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import copy
file_full_path = "/home/tianyu/software/IdeaProject/computer_vision_algorithm/rice.jpg"
image = cv2.imread(file_full_path)
#将彩色图像转换成灰度图像
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#阈值填充
_,bw = cv2.threshold(grayImage, 0, 0xff, cv2.THRESH_OTSU)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
bw = cv2.morphologyEx(bw, cv2.MORPH_OPEN, element)
seg = copy.deepcopy(bw)
#轮廓
contours, hierarchy = cv2.findContours(seg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
count = 0
for i in range(len(contours), 0, -1):
    c = contours[i - 1]
    area = cv2.contourArea(c)
    if area < 10:
        continue
    count = count + 1
    print("blob", i, ":", area)

    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0xff), 1)
    cv2.putText(image, str(count), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 0xff, 0))

print("米粒数量：", count)

cv2.imshow("Source Image", image)
cv2.imshow("threshold Image", bw)
cv2.waitKey()
cv2.destroyAllWindows()