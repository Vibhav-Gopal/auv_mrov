#include "ros/ros.h"
#include "materov22_pioneer/motion_command_msg.h"

using namespace std;

void displayHelp(void)
{
    cout << "Commands : \n w - Forward \t s - backward \t a - left\t d - right \n i - up \t k - down \t j - yaw_left \t l - yaw_right \t p - sprint \n x - stop \t r - resume \t n - lights on \t m - lights off \n q - turn to given angle \n" << endl;
}

int main(int argc, char** argv)
{
    ros::init(argc,argv,"output");

    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<materov22_pioneer::motion_command_msg>("/motion_command",1000);

    materov22_pioneer::motion_command_msg i;

    char input;
    int angle;

    ros::Rate loop_rate(10);

    while (ros::ok())
    {
        
        input = getchar();

        switch(input)
        {
            //forard
            case 'w':
            {
                i.command = 0;

                pub.publish(i);
                break;
            }

            //backward
            case 's':
            {
                i.command = 1;
                pub.publish(i);

                break;
            }

            //left
            case 'a':
            {
                i.command = 2;
                pub.publish(i);

                break;
            }

            //right
            case 'd':
            {
                i.command = 3;
                pub.publish(i);

                break;
            }

            //up
            case 'i':
            {
                i.command = 4;
                pub.publish(i);

                break;
            }

            //down
            case 'k':
            {
                i.command = 5;
                pub.publish(i);

                break;
            }

            //yaw_left
            case 'j':
            {
                i.command = 6;
                pub.publish(i);

                break;
            }

            //yaw_right
            case 'l':
            {
                i.command = 7;
                pub.publish(i);

                break;
            }

            //sprint
            case 'p':
            {
                i.command = 8;
                pub.publish(i);

                break;
            }

            //stop
            case 'x':
            {
                i.command = 9;
                pub.publish(i);

                break;
            }

            //resume
            case 'r':
            {
                i.command = 10;
                pub.publish(i);

                break;
            }

            //turn to given direction
            case 'q':
            {
                i.command = 11;

                cout<<"\nEnter the angle : ";
                cin >> angle;

                i.angle = angle;

                pub.publish(i);

                break;
            }

            //lights on
            case 'n':
            {
                i.command = 12;
                pub.publish(i);

                break;
            }

            //lights off
            case 'm':
            {
                i.command = 13;
                pub.publish(i);

                break;
            }

            case 'h':
            {
                displayHelp();

                break;
            }
        }


    ros::spinOnce();

    loop_rate.sleep();
    }
    return 0;
}
