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
'''
    第一个参数是寻找轮廓的图像
    第二个图像表示轮廓的检索模式
    RETR_EXTERNAL：检测外轮廓
    RETR_LIST:检测的轮廓不建立等级关系
    RETR_CCOMP:建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息，如果内控内还有一个联通物体，这个物体的边界也在顶层
    RETR_TREE:建立一个等级树结构的轮廓
    
    第三个参数表示轮廓的近似办法
    CHAIN_APPROX_NONE:存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max(abs(x1 - x2), abs(y2 -y1)) == 1
    CHAIN_APPROX_SIMPLE:压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的重点坐标，例如一个矩形轮廓秩序四个点来保存轮廓信息
    CHIAN_APPROX_TC89_L1,CV_CHAIN_TC89_KCOS使用tech-Chinl chain近似算法
'''
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