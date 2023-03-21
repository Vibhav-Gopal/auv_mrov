#ifndef ROS_FUNCTS_H
#define ROS_FUNCTS_H
void ros_init(int argc, char** argv);
void publishPWMValues(int* pwm_values);
void changeLEDState(bool );
void checkForCallBack();
#endif