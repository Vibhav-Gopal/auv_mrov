// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Copyright Drew Noakes 2013-2016

#include "joystick.h"
#include <unistd.h>
#include"ros/ros.h"
#include"std_msgs/String.h"
#include "materov22_pioneer/motion_command_msg.h"
#include"../thrustered_vehicle_motioncontroller/thrustered_vehicle_motion_controller.h"
#include<iostream>
#include<cmath>
#include<vector>
#include<sstream>
#include"motion_commands.h"
#define RAD2DEG 57.2975

using namespace std;
int quad;

int main(int argc, char** argv)
{
  ros::init(argc, argv, "input");

  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<materov22_pioneer::motion_command_msg>("/motion_command",1);

  std_msgs::String j;

  materov22_pioneer::motion_command_msg i;

  std::vector<int>arr_2;

  std::vector<int>arr_3;

  std::vector<int>arr_4;

  ThrusteredVehicleMotionController obj;
  
  float x,y,z;

  // Create an instance of Joystick
  Joystick joystick("/dev/input/js0");

  // Ensure that it was found and that we can use it
  if (!joystick.isFound())
  {
    printf("Joystick is not connected :(\n");
    exit(1);
  }

  while (true)
  {
    // Restrict rate
    usleep(1000);

    // Attempt to sample an event from the joystick
    JoystickEvent event;
    if (joystick.sample(&event))
    {
      if (event.isButton() && event.value != 0)
      {
        //L1 - Up
        if(event.number == 4)
        {
          i.command = UP;

          pub.publish(i);

          obj.setHeaveThrust(100);
        }

        //R1 - Down
        else if(event.number == 5)
        {
          i.command = DOWN;

          pub.publish(i);

          obj.setHeaveThrust(-100);
        }

        //L2 - Yaw left
        else if(event.number == 6)
        {
          i.command = YAW_LEFT;

          pub.publish(i);
        }

        //R2 - Yaw right
        else if(event.number == 7)
        {
          i.command = YAW_RIGHT;

          pub.publish(i);
        }

        //Button 1 - Sprint
        else if(event.number == 0)
        {
          i.command = SPRINT;

          pub.publish(i);
        }

        //Button 2 - Resume
        else if(event.number == 1)
        {
          i.command = 10;

          pub.publish(i);
        }

        //Button 4 - Stop
        else if(event.number == 3)
        {
          i.command = STOP;

          pub.publish(i);
        }

        //Button L3 - Lights on 
        else if(event.number == 10)
        {
          i.command = LIGHTS_ON;

          pub.publish(i);
        }

        //Button R3 - Lights off 
        else if(event.number == 11)
        {
          i.command = LIGHTS_OFF;

          pub.publish(i);
        }

      }
      
      else if (event.isAxis())
      {
          if(event.number == 6)
          {
            //Backward is pressed
            if(event.value > 0)
            {
              i.command = BACKWARD;
              
              pub.publish(i);
            }
          
            //Forward is pressed
            if(event.value < 0)
            {
              i.command = FORWARD;
              
              pub.publish(i);
            }
          }

          else if(event.number == 5)
          {
            //Right is pressed
            if(event.value > 0)
            {
              i.command = RIGHT;

              pub.publish(i);
            }
            //Left is pressed
            if(event.value < 0)
            {
              i.command = LEFT;

              pub.publish(i);
            }
          }

          else if(event.number == 2)
          {
              // arr_2.push_back(event.value);

              y = event.value;
          }
          
          else if(event.number == 3)
          {
              // arr_3.push_back(event.value);

              x = event.value;
          }

          else if(event.number == 4)
          {
              // arr_4.push_back(event.value);

              z = event.value;
          }

          if(y!=0)
          {            
            float an = -x/y;

            int angle = int(atan(an) * RAD2DEG);

            if(z<0)
            {
              quad = 1;
            }
            else if(z>0)
            {
              quad = 0;
            }

            if(quad == 0)
            {
              angle = int(angle + 180);
            }

            if(quad ==1 && angle < 0)
            {
              angle = int(angle + 360);
            }

            cout << "\nAngle : " << angle << endl;

            i.command = TURN_TO_GIVEN_DIRECTION;
            
            i.angle = angle;
            
            pub.publish(i); 

            arr_3.clear();

            arr_2.clear(); 
            
          }

          else if(x != 0 && y == 0)
          {
            int angle = 270;

            if(quad == 1)
            {
              angle = 90;
            }

            cout << "\nAngle : "<< angle << endl;

            i.command = TURN_TO_GIVEN_DIRECTION;  
            
            i.angle = angle;

            pub.publish(i);

            arr_3.clear();

            arr_2.clear();
          }

            
          }
          
      }
    }
  }

