
from os import spawnl
import cv2
import glob
import numpy as np
import os

class Teste:
    def __init__(self):
        self.xstring = str
        self.ystring = str
        self.h_t = str
        self.w_t = str
        self.space = " "
        self.zero = "0"

ed = Teste()
i= 0
cv_img = []

def load_images():
    for img in glob.glob("/home/franciscofilho/Makesense_Python/*png"):
        n = cv2.imread(img)
        h,w,_ = n.shape
        cv_img.append(n)
    return cv_img,h,w,_

list_img,h,w,_ = load_images()

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
z = 1
ROI_number = 1

def draw_circle(event,x,y,flags,param):
        
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(list_img[i],(ix,iy),(x,y),(0,255,0),2)
            print(ix,iy,x,y,w,h)
            print(abs(ix-x))
            
            xcenter = (ix + abs(ix-x)/2) / w
            print(ix,abs(ix-x),w)
            ycenter = (iy + abs(iy-y)/2) / h
            w_t = abs(ix-x) / w
            h_t = abs(iy-y) / h

            ed.xstring = "{:.6f}".format(xcenter)
            ed.ystring = "{:.6f}".format(ycenter)
            ed.w_t = "{:.6f}".format(w_t)
            ed.h_t = "{:.6f}".format(h_t)
        
        with open('/home/franciscofilho/Makesense_Python/image_{}.txt'.format(ROI_number), 'a') as f:
            f.write(ed.zero + ed.space + ed.xstring + ed.space + ed.ystring + ed.space + ed.w_t + ed.space + ed.h_t)
            f.write('\n')
                

    

cv2.namedWindow('image',cv2.WINDOW_GUI_NORMAL)
cv2.setMouseCallback('image',draw_circle)


while(i < len(list_img)):
 cv2.imshow('image',list_img[i])
 
 
 k = cv2.waitKey(1) & 0xFF
 if k == ord('m'):
    i = i+1
    ROI_number += 1
 elif k == 27:
    break

cv2.destroyAllWindows()  





