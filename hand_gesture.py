# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:23:48 2019

@author: hamed
"""

import cv2
import numpy as np
from scipy.spatial import distance


hand_img = cv2.imread("5.jpg")

hsv_img = cv2.cvtColor(hand_img, cv2.COLOR_BGR2HSV)

lower_band = np.array([0, 23, 0])
upper_band = np.array([255, 189, 255])

dislist = []

mask = cv2.inRange(hsv_img, lower_band, upper_band)
_, cnts,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

c = cnts[0]
print(c)
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

M = cv2.moments(c)

cX = int(M["m10"]/M["m00"])
cY = int(M["m01"]/M["m00"])

center = (cX, cY)

D1 = distance.euclidean(extLeft, center)
D2 = distance.euclidean(extRight, center)
D3 = distance.euclidean(extTop, center)
D4 = distance.euclidean(extBot, center)

dislist.append(D1)
dislist.append(D2)
dislist.append(D3)
dislist.append(D4)

A = int(0.65 *max(dislist))

cv2.circle(mask, (cX, cY), A, (0, 255, 0), -1)

_, cnts,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("number of finger is:" ,len(cnts)-1)

cv2.imshow("hand", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
