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
        #print(i)
        #拼接绝对路径
        path2 = os.path.join(path,i)
        print(path2)
        if os.path.isdir(path2):
            #判断如果是文件夹,调用本身
            func(path2)
        else:
            imageFullPath = path + i
            print(imageFullPath)
            if(imageFullPath.endswith(".jpg") or imageFullPath.endswith(".png")):
                image = cv2.imread(path + i)
                b, g, r = cv2.split(image)
                histImgB = calcAndDrawHist(b, [255, 0, 0])
                histImgG = calcAndDrawHist(g, [0, 255, 0])
                histImgR = calcAndDrawHist(r, [0, 0, 255])

                cv2.imshow("histImgB", histImgB)
                cv2.imshow("histImgG", histImgG)
                cv2.imshow("histImgR", histImgR)
                cv2.imshow(i + "Image", image)
                cv2.waitKey()
                cv2.destroyAllWindows()
def calcAndDrawHist(image, color):
    #计算灰度直方图
    '''
    其中第一个参数必须用方括号括起来。
    第二个参数是用于计算直方图的通道，这里使用灰度图计算直方图，所以就直接使用第一个通道；
    第三个参数是Mask，这里没有使用，所以用None。
    第四个参数是histSize，表示这个直方图分成多少份（即多少个直方柱）。第二个例子将绘出直方图，到时候会清楚一点。
    第五个参数是表示直方图中各个像素的值，[0.0, 256.0]表示直方图能表示像素值从0.0到256的像素。
    最后是两个可选参数，由于直方图作为函数结果返回了，所以第六个hist就没有意义了（待确定）
    最后一个accumulate是一个布尔值，用来表示直方图是否叠加。
    '''
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9* 256);

    for h in range(256):
        intensity = int(hist[h]*hpt/maxVal)
        cv2.line(histImg,(h,256), (h,256-intensity), color)
    return histImg

func(file_full_path)

