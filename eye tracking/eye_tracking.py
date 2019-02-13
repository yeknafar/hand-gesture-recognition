# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:23:07 2019

@author: hamed
"""

import cv2

cap = cv2.VideoCapture("eye.mp4")

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (486,286))

font = cv2.FONT_HERSHEY_COMPLEX

direction = "center"

while True:
    
    _, frame = cap.read()
    
    if frame is None:
        break
    
    roi = frame[211:497, 445:931]
    
    roi_copy = roi
    
    height, width, _ = roi.shape
    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    
    _, thresh = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY_INV)
    dilate = cv2.dilate(thresh, (5, 5), iterations = 4)
    
    _, cnts, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:
        cnts = sorted(cnts ,key = cv2.contourArea, reverse = True)[0]
        
        (x, y, w, h) = cv2.boundingRect(cnts)
        
        cv2.rectangle(roi, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.line(roi, (x+int(w/2), 0), (x+int(w/2), height), (0, 255, 0), 2) 
        cv2.line(roi, (0, y+int(h/2)), (width, y+int(h/2)), (0, 255, 0), 2)
        
                
        if (x - width//2) > 20:
            direction = "dir: right"
            cv2.putText(roi, direction ,(30,30), font, 0.95, (255, 255, 255), 2)
        
        elif (width//2 - x) > 20:
            direction = "dir: left"
            cv2.putText(roi, direction ,(30,30), font, 0.95, (255, 255, 255), 2)
        
        elif abs(width//2 - x) < 20 :
            direction = "dir: center"
            cv2.putText(roi, direction ,(30,30), font, 0.95, (255, 255, 255), 2)
            
            if abs(height//2 - y) > 40:
                cv2.putText(roi, "" ,(30,30), font, 0.95, (255, 255, 255), 2)
                direction = "dir: up"
            
            elif abs(y - height//2) > 40:
                cv2.putText(roi, "" ,(30,30), font, 0.95, (255, 255, 255), 2)
                direction = "dir: down"
                
            cv2.putText(roi, direction ,(30,30), font, 0.95, (255, 255, 255), 2)
           
    except:
        cv2.putText(roi,"not detected" ,(30,30), font, 0.75, (0, 0, 255), 2)
    
    cv2.imshow("eye", roi)
    out.write(roi)
    cv2.waitKey(1)
    
    if cv2.waitKey(30) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()