# RoboticsYouBot
Kuka YouBot

This project solves inverse and direct kinematics in Kuka YouBot Manipulator

To run this project RosCore on YouBot must be activated.
To do so:

$ roscore

In the other terminal Youbot driver must be activated:

$ roslaunch youbot_driver_ros_interface youbot_driver.launch

If you don't have the driver instlled:
All instructions to install driver can be found there: http://www.youbot-store.com/wiki/index.php/ROS_Wrapper Please be aware of the ROS version that you are using.

To run this code it must be placed in the src folder of correct workspace.
To try it:

$ python main.py

 Main function creates the instance of class MyRobot and calls function run()

 Function run() starts demonstative program in witch user have several options to choose. (Instructions appear on the screen)

 Write:
     >>>direct<<< to calculate direct kinematics
     >>>inverse<<< to calculate inverse kinematics
     >>>setangles<<< to enter desired joint values
     >>>home<<< to go to the home position
     >>>candle<<< to go to the candle position
     >>>pick<<< to pick object in front of robot
     >>>place<<< to place object on the robot
     >>>pick&place<<< to pick object and place it on the robot
     >>>demo<<< to see the demonstration of all pick and place possibilities
     >>exit<<< to exit


Direct kinematics is solved by Denavit-Hartenberg parameters



Inverse kinematics is the reverse proces to direct kinematics. Through it we compute the joint parameters that achieve a specified position of the end-effector.

We assume that:
 - first join is moving only into 5 positions (it could be also computed as arctan2(x,y) but it require some assumptions). In our project:
- right – to pick/place something on the right
- left
- front
- back on the left – to pick/place something at the back (slightly on the left)
- back on the right – to pick/place something at the back (slightly on the right)

The second assumption is that we know what is the required position of the last joint with respect to horizontal plane. -90 degree means that end effector is directed towards the ground.

With those assumptions to solve inverse problem we just need to solve 3-DOF planar manipulator. For more detales see the report

Robot performance: https://drive.google.com/file/d/1Qd1oa_3Lqwf5Xv1-zND4OBbbQQkDWGxz/view?usp=sharing
