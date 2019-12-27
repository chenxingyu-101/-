import cv2
import serial
#图像采集顺序R8、U6、U2、F6、F2、L6、L2、B6、B2、D6、D2
H=600
W=600
id1=1
COM='COM4'
#1.采集R面
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/R8.jpg",cv2.resize(frame, (W, H))) 
cap.release()

print('采集R8完成')


#2.采集U面6块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
data=b'S'
ser.write(data)
print('等待返回2')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成，可以采集图像')
ser.close()

cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/U6.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集U6完成')

#3.采集U面2块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回3')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/U2.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集U2完成')

#4.采集F面六块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回4')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/F6.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集F6完成')

#5.采集F面2块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回5')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/F2.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集F2完成')

#6.采集L面6块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回6')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/L6.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集L6完成')

#7.采集L面2块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回7')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/L2.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集L2完成')

#8.采集B面6块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回8')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/B6.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集B6完成')

#9.采集B面2块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回9')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/B2.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集B2完成')

#10.采集D面6块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回A')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/D6.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集D6完成')

#11.采集D面2块
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回B')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('电机旋转完成')
ser.close()
cap = cv2.VideoCapture(id1)
i=20
while i>0:
    i=i-1
    ret, frame = cap.read() 
    cv2.imwrite("C:/Documents/picture/D2.jpg",cv2.resize(frame, (W, H))) 
cap.release()
print('采集D2完成')

#12.复位
ser = serial.Serial()
ser.port = COM
ser.baudrate = 9600
ser.timeout = 0.2
ser.open()
ser.write(b'S')
print('等待返回C')
while True:
    data = ser.read(10)
    if data != b'':
        print(data)
        break
print ('采集图像完成')
ser.close()
#****************************************************************************
#提取图像信息
from get_color_R8 import get_color_R8

from get_color_U6 import get_color_U6
from get_color_U2 import get_color_U2

from get_color_F6 import get_color_F6
from get_color_F2 import get_color_F2

from get_color_L6 import get_color_L6
from get_color_L2 import get_color_L2

from get_color_B6 import get_color_B6
from get_color_B2 import get_color_B2

from get_color_D6 import get_color_D6
from get_color_D2 import get_color_D2
y=[0,84,61,58,315,0,143,543,482,441]
x=[0,146,263,357,143,0,360,166,273,351]

s49,s51=get_color_B2(y,x)
s46,s47,s48,s52,s53,s54=get_color_B6(y,x)
s31,s33=get_color_D2(y,x)
s28,s29,s30,s34,s35,s36=get_color_D6(y,x)
s22,s24=get_color_F2(y,x)
s19,s20,s21,s25,s26,s27=get_color_F6(y,x)
s38,s44=get_color_L2(y,x)
s37,s39,s40,s42,s43,s45=get_color_L6(y,x)
s10,s11,s12,s13,s15,s16,s17,s18=get_color_R8(y,x)
s4,s6=get_color_U2(y,x)
s1,s2,s3,s7,s8,s9=get_color_U6(y,x)

s5='U'
s23='F'
s41='L'
s32='D'
s14='R'
s50='B'

s=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20+s21+s22+s23+s24+s25+s26+s27+s28+s29+s30+s31+s32+s33+s34+s35+s36+s37+s38+s39+s40+s41+s42+s43+s44+s45+s46+s47+s48+s49+s50+s51+s52+s53+s54
print('魔方色块信息:',s)
countD=s.count('D',0,len(s))
countU=s.count('U',0,len(s))
countR=s.count('R',0,len(s))
countB=s.count('B',0,len(s))
countF=s.count('F',0,len(s))
countL=s.count('L',0,len(s))
if countD==9 and countU==9 and countR==9 and countB==9 and countF==9 and countL==9:
    print('识别无误')
else:
    print('D',countD)
    print('U',countU)
    print('R',countR)
    print('B',countB)
    print('F',countF)
    print('L',countL)
    print('识别出错')
    #while 1:
     #   pass
#******************************************************************************
#处理图像信息
import kociemba as kb
from str_translate import str_translate
s_solve=(kb.solve(s))
print(s_solve)
motor=str_translate(s_solve)
print(motor)
i=0
while i<len(motor):
    ser = serial.Serial()
    ser.port = COM
    ser.baudrate = 9600
    ser.timeout = 0.2
    ser.open()
    if ser.isOpen():
        data = motor[i]    
        ser.write(data)
    else:
        print ('串口未打开')
    i=i+1
    while True:
        print('等待返回')
        data = ser.read(10)
        if data != b'':
            print(data)
            break
    ser.close()
print ('魔方还原完成')
    
