
import os
import cv2
import glob
from pathlib import Path
import math


cv_img = [] ; drawing = False ; mode = True ; z = 1 ; ix,iy = -1,-1

class Teste:
    def __init__(self):
        self.xstring = str
        self.ystring = str
        self.h_t = str
        self.w_t = str
        self.space = " "
        self.zero = "0"
        self.index = 0
        self.roi_number = 0
        self.filename = []


def criar_tela():
    cv2.namedWindow('image',cv2.WINDOW_GUI_NORMAL)
    cv2.setMouseCallback('image',draw_circle)

def load_images():
    for img in glob.glob("/home/francsicofilho/Documentos/Yolo_Format_Teste/*png"):
        n = cv2.imread(img)
        h,w,_ = n.shape
        cv_img.append(n)
    return cv_img,h,w,_


def split_files():
    path = '/home/francsicofilho/Documentos/Yolo_Format_Teste'
    ed.filename = [f for f in os.listdir(path) if f.endswith('.png')]
    i=0
    for g in ed.filename:
        name = ed.filename[i]
        ed.filename[i] = os.path.splitext(name)[0]
        i=i+1
    print(ed.filename)

def delete_files():
    directory = "/home/francsicofilho/Documentos/Yolo_Format_Teste"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".txt")]
    for file in filtered_files:
	    path_to_file = os.path.join(directory, file)
	    os.remove(path_to_file)

def menu():
    esc = input("Desaja apagar todas as labels da pasta? yes | no\n")
    if (esc=="yes"):
        delete_files()
        main()
    elif(esc == "no"):
        print("Ok!")
        main()
    else:
        print("Nenhuma das alternativas")
        menu()

def draw_circle(event,x,y,flags,param):
        
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(list_img[ed.index],(ix,iy),(x,y),(0,255,0),2)
            im2 = list_img.copy()
            # print(ix,iy,x,y,w,h)
            # print(abs(ix-x))
            # print(ed.index)
            # print(ed.roi_number)
            
            xcenter = (ix + abs(ix-x)/2) / w
            print(ix,abs(ix-x),w)
            ycenter = (iy + abs(iy-y)/2) / h
            w_t = abs(ix-x) / w
            h_t = abs(iy-y) / h

            ed.xstring = "{:.6f}".format(xcenter)
            ed.ystring = "{:.6f}".format(ycenter)
            ed.w_t = "{:.6f}".format(w_t)
            ed.h_t = "{:.6f}".format(h_t)
            
            
            split_files()
        with open('/home/francsicofilho/Documentos/Yolo_Format_Teste/{}.txt'.format(ed.filename[ed.index]), 'a') as f:
            f.write(ed.zero + ed.space + ed.xstring + ed.space + ed.ystring + ed.space + ed.w_t + ed.space + ed.h_t)
            f.write('\n')
            print(ed.index)
            
                
def main():
    criar_tela()
    while(ed.index < len(list_img)):
        cv2.imshow('image',list_img[ed.index])
        k = cv2.waitKey(1) & 0xFF
        if k == ord(' '):
            ed.index = ed.index+1
            ed.roi_number += 1
        elif k == 27:
            break
    cv2.destroyAllWindows()
 

ed = Teste() ; list_img,h,w,_ = load_images()
menu()

