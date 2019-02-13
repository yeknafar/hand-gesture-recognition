# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:40:24 2019

@author: hamed
"""

import cv2
import imutils

book1= cv2.imread("book1.jpg")
book2 = cv2.imread("book2.jpg", 0)

book1 = imutils.resize(book1, width=500)
book2 = imutils.resize(book2, width=500)

sift = cv2.xfeatures2d.SIFT_create()
    
kp1, des1 = sift.detectAndCompute(book1,None)
kp2, des2 = sift.detectAndCompute(book2, None)

#bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
#match = bf.match(des1, des2)

#match = sorted(match, key = lambda x:x.distance)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)

match = bf.knnMatch(des1, des2, k=2)

good_point = []

for m, n in match:
    if m.distance < 0.6 * n.distance:
        good_point.append(m)
        

matching_result = cv2.drawMatches(book1, kp1, book2, kp2,  good_point, None)

cv2.imshow("hamed", matching_result)

cv2.waitKey(0)
cv2.destroyAllWindows()