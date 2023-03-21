cmake_minimum_required(VERSION 3.0.2)
project(materov22_pioneer)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
   FILES
   motion_command_msg.msg
   pwm_values_msg.msg
   sensor_data_msg.msg
controller.msg
axes.msg
 )

 generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  
  CATKIN_DEPENDS message_runtime 
  )




include_directories(include 

   ${catkin_INCLUDE_DIRS}
)



add_subdirectory(src)
