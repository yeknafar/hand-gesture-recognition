# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:36:27 2019

@author: hamed
"""

import cv2

img = cv2.imread("image.jpg")
template = cv2.imread("template.png")

h, w, _ = template.shape

coor_img = cv2.matchTemplate(img, template, method = cv2.TM_SQDIFF)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(coor_img)

top_left = min_loc
bottom_right = (top_left[0]+w, top_left[1]+h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

cv2.imshow("coor img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()