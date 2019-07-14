#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os

file_full_path = "/home/tianyu/software/IDEAProjects/computer_vision_algorithm/data/"
lenaImage = cv2.imread("aero1.jpg")

imageList = []

def func(path):
    for i in os.listdir(path):
        #拼接绝对路径
        path2 = os.path.join(path,i)
        if os.path.isdir(path2):
            #判断如果是文件夹,调用本身
            func(path2)
        else:
            imageFullPath = path + i
            print(imageFullPath)
            if(imageFullPath.endswith(".jpg") or imageFullPath.endswith(".png")):
                image = cv2.imread(path + i)
                cv2.imshow(i, image)
                '''
                第一个为原图像
                第二个为阈值0，OTSU会自动寻找阈值
                第三个为高于阈值时赋予的新值
                第四个为在这里选择大津算法。
                该函数有两个返回值，第一个retVal（得到的阈值值），第二个就是阈值化后的图像。
                '''
                ret1, thresHoldImage = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
                cv2.imshow('colorhist',thresHoldImage)

                cv2.waitKey()
                cv2.destroyAllWindows()
func(file_full_path)

