import numpy as np
import math
import rospy
from brics_actuator.msg import JointPositions, JointValue, Poison
from myRobotClass import myRobot
from talker import talker
from direct import directCount
import string





def main():
    rob = myRobot()
    rob.run()
 

if __name__=="__main__":
    main()
