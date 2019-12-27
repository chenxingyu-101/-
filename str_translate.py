def str_translate(s='12 34 5678'):
    my_s=s.replace("'","1")
    my_list=my_s.split()
    motor=list()
    motor_dir=list()
    i=0
    while i<len(my_list):

        if my_list[i]=='U':
            motor.append(b'A')# T代表正转90°（魔方面顺时针）
        if my_list[i]=='U1':
            motor.append(b'B')
        if my_list[i]=='U2':
            motor.append(b'C')
            
        if my_list[i]=='R':
            motor.append(b'D')
        if my_list[i]=='R1':
            motor.append(b'E')
        if my_list[i]=='R2':
            motor.append(b'F')

        if my_list[i]=='F':
            motor.append(b'G')
        if my_list[i]=='F1':
            motor.append(b'H')
        if my_list[i]=='F2':
            motor.append(b'I')

        if my_list[i]=='D':
            motor.append(b'J')
        if my_list[i]=='D1':
            motor.append(b'K')
        if my_list[i]=='D2':
            motor.append(b'L')

        if my_list[i]=='L':
            motor.append(b'M')
        if my_list[i]=='L1':
            motor.append(b'N')
        if my_list[i]=='L2':
            motor.append(b'O')

        if my_list[i]=='B':
            motor.append(b'P')
        if my_list[i]=='B1':
            motor.append(b'Q')
        if my_list[i]=='B2':
            motor.append(b'R')
        i=i+1
    return motor
