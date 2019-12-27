import cv2
def get_color(y,x):
    m=0
    n=0
    v=0
    img = cv2.imread('C:/Documents/picture/R8.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(5):
        for j in range(5):
            s=hsv[y+i, x+j]           
            m=m+s[0]#获得H（色相）  opencv中：0<=H<=179
            n=n+s[1]#获得S（饱和度）opencv中：0<=S<=255
            v=v+s[2]#获得V（亮度）  opencv中：0<=V<=255
            s=hsv[y-i, x-j] 
            m=m+s[0]#获得H
            n=n+s[1]#获得S
            v=v+s[2]
    m=m//50
    n=(n//50)
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
def get_color_R8(y=list(),x=list()):
    s10=get_color(y[1],x[1])
    s11=get_color(y[2],x[2])
    s12=get_color(y[3],x[3])
    s13=get_color(y[4],x[4])
    s15=get_color(y[6],x[6])
    s16=get_color(y[7],x[7])
    s17=get_color(y[8],x[8])
    s18=get_color(y[9],x[9])   
    return s10,s11,s12,s13,s15,s16,s17,s18


