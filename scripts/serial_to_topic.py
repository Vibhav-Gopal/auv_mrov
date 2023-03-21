import serial
import rospy
from std_msgs.msg import Float32
port = '/dev/ttyACM0'
rate = 115200
arduino = serial.Serial(port=port,baudrate=rate)

rospy.init_node('yaw_data')

yaw = rospy.Publisher("/yaw",Float32, queue_size=1000)

def getYaw():
    data = arduino.readline()
    data = data.decode()
    try: data = float(data)
    except: return 0
    return data
while(1):
    data = getYaw()
    yaw.publish(data)
