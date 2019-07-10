#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
file_full_path = "/home/tianyu/software/IdeaProject/computer_vision_algorithm/lena.jpg"
image = cv2.imread(file_full_path)

#均值滤波
blurExImage = cv2.blur(image, (5, 5))
cv2.imshow("Source Image", image)
cv2.imshow("blur Image", blurExImage)
cv2.waitKey()
cv2.destroyAllWindows()
