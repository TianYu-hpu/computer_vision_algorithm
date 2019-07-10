#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
file_full_path = "/home/tianyu/software/IdeaProject/computer_vision_algorithm/lena.jpg"
image = cv2.imread(file_full_path)

#形态学滤波
#设置核
kernel = np.ones((5,5),np.uint8)
morphologyExOpenImage = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Source Image", image)
cv2.imshow("morphologyEX open Image", morphologyExOpenImage)
cv2.waitKey()
cv2.destroyAllWindows()