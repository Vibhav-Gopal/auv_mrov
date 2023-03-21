#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from calc import process
from joy import ping
import signal
#a0_a1_a2_a3_at1_at2_b1_..._bn
# where a0 is left joystick x axis and a2 is right joystick x axis
#the axes range from -1 to 1 and the button only 0/1


#0 is top -0 is bottom, 90 is right, -90 is left
# UP is 0degrees
# RIGHT is 90 degrees
# DOWN is 180 degrees
# LEFT is 270 degrees

dat = rospy.Publisher("/joydata",String, queue_size=1000)

def handler(signum, frame):
    
    exit(0)

signal.signal(signal.SIGINT, handler)

def callback(state,state_labels):
    
    

    #ljoy,ljoystr,rjoy,rjoystr,ltrig,rtrig = process(state)
    finData = list()
    finData = process(state)
    
    
    tempLis = state
    for i in range(len(tempLis)):
        tempLis[i] = round(tempLis[i],2)
        
    finData = tempLis
    
    finData = list(map(str,finData))
    dataString = '_'.join(finData)
    print("Data is",dataString)
    sender(dataString)    

def sender(toSend):
    dat.publish(toSend)

if __name__ == '__main__':
    rospy.init_node('joystick_control')
    
    ping(callback)

    rospy.spin()
    