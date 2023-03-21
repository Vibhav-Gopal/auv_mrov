#!/usr/bin/env python3
import sys
sys.path.append('/home/r2d2/mrov_ws/devel/lib/')
import rospy
import motion_controller as m
from std_msgs.msg import String
cholan = m.ThrusteredVehicleMotionController()

cholan.setHeaveControlMode(1)
cholan.setSurgeControlMode(1)
cholan.setYawControlMode(1)


#help(m)
def mul(x):
    return 100*x
def call(data):
    
    lis = data.data.split('_')
    lis = list(map(float,lis))
    lis = list(map(mul,lis))
    lis[5] = lis[5]+100
    lis[5]  = lis[5]/2
    lis[5] = round(lis[5])
    lis[5] = -1*lis[5]
    
    lis[4] = lis[4]+100
    lis[4]  = lis[4]/2
    lis[4] = round(lis[4])
    
    lis[1] = -1*lis[1]
    
    thrust = lis[4]+lis[5]
    surge = lis[1]
    yaw = lis[2]
    
    reset = lis[10]
    cholan.setHeaveThrust(thrust)
    cholan.setSurgeThrust(surge)
    cholan.setYawThrust(yaw)
    if(reset ==100):
        cholan.resetAllThrusters()
    cholan.refresh()
    if int(thrust) >= -7 and int(thrust) <=7:
        thrust =0
        
    if int(surge) >= -7 and int(surge) <=7:
        surge =0
        
    if int(yaw) >= -7 and int(yaw) <=7:
        yaw =0
    
    print("Thrust:",thrust,"Surge:",surge,"Yaw",yaw,"Reset-",reset)
    pass
rospy.init_node("listendata")
rospy.Subscriber('/joydata', String,call)
rospy.spin()