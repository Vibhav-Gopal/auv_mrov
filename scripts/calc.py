from math import *
def process(stet):
    #data = list(map(float,stet.split('_')))
    data = stet
    try:
        
        leftangle = degrees(atan(data[0]/data[1]))

    except(ZeroDivisionError):
        if(data[0]==-1):
            leftangle = -90
        else:
            leftangle = 90 
    
    try:
        
        rightangle = degrees(atan(data[2]/data[3]))

    except(ZeroDivisionError):
        if(data[2]==-1):
            rightangle = -90
        else:
            rightangle = 90

    lstrength = sqrt(data[0]**2 + data[1]**2)
    rstrength = sqrt(data[2]**2 + data[3]**2)

    if str(leftangle)[0] == '-' and leftangle==0:
        leftangle  = 180
    elif str(leftangle)[0] == '-' and leftangle==-90:
        leftangle = 270

    if str(rightangle)[0] == '-' and rightangle==0:
        rightangle  = 180
    elif str(rightangle)[0] == '-' and rightangle==-90:
        rightangle = 270

    if data[0]>0 and data[1]<0:
        leftangle = 180+leftangle
    elif data[0]<0 and data[1]<0:
        leftangle=180+leftangle
    elif data[0]<0 and data[1]>0:
        leftangle = 270-leftangle

    if data[2]>0 and data[3]<0:
        rightangle = 180+rightangle
    elif data[2]<0 and data[3]<0:
        rightangle=180+rightangle
    elif data[2]<0 and data[3]>0:
        rightangle = 270-rightangle

    ltstrength = (data[4]+1)/2
    rtstrength = (data[5]+1)/2   
    temp = [leftangle,lstrength, rightangle, rstrength, ltstrength,rtstrength]
    for i in range(len(temp)):
        temp[i] = round(temp[i],2)
    leftangle,lstrength, rightangle, rstrength, ltstrength,rtstrength = temp
    return leftangle,lstrength, rightangle, rstrength, ltstrength,rtstrength
