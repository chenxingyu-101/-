# -*- coding:utf-8 -*-
import cv2
def get_color(y,x):
    m=0
    n=0
    v=0
    img = cv2.imread('C:/Documents/picture/B2.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(5):
        for j in range(5):
            s=hsv[y+i, x+j]           
            m=m+s[0]#获得H
            n=n+s[1]#获得S
            v=v+s[2]
            s=hsv[y-i, x-j] 
            m=m+s[0]#获得H
            n=n+s[1]#获得S
            v=v+s[2]
    m=m//50
    n=n//50
    v=(v//50)/255
    if m<8 and n>80:
        return 'L'         
    elif 8<m<23 and n>80:
        return 'R'
    elif 23<m<40 and n>80:
        return 'B'
    elif 43<m<80 and n>80:
        return 'U'
    elif 95<m<115 and n>80:
        return 'D'
    elif n<80:
        return 'F'
    else:
        return '*'
def get_color_B2(y=list(),x=list()):
    s49=get_color(y[2],x[2])
    s51=get_color(y[8],x[8])
    return s49,s51

