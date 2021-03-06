# -*- coding:utf-8 -*-
import cv2
def get_color(y,x):
    m=0
    n=0
    v=0
    img = cv2.imread('C:/Documents/picture/U6.jpg')
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
def get_color_U6(y=list(),x=list()):
    s1=get_color(y[3],x[3])
    s2=get_color(y[6],x[6])
    s3=get_color(y[9],x[9])
    s7=get_color(y[1],x[1])
    s8=get_color(y[4],x[4])
    s9=get_color(y[7],x[7])
   
    return s1,s2,s3,s7,s8,s9

