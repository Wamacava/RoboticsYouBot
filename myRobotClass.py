#myRobot class contains methods necessary to perform pick and place operation
from inverse import inverseCount
import numpy as np
import math
import rospy
from talker import talker
from direct import directCount

class myRobot:
    Q = [0, 0.3, -0.05, 0, -90]  # init values ???
    G= [0, 0] # gripper Left, Right

    # Link Length in centimeters:
    L1 = 14.7
    L2 = 15.5
    L3 = 13.5
    L4 = 8.1
    L5 = 13.7

    def __init__(self):

        print('Hello')
        #?

    def pubAngles(self, Q):

        try:
            talker(self.Q)
    	    print("done")
        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

    def pubGripper(self, G):
        print('')


    def closeGripper(self):
        print('')

    def directKinematics(self):
	
	x, y, z = directCount(self.Q)

	print('x, y, z: ', x, y, z)


    def inverseKinematics(self, x, y, z, alfa, beta):

        self.Q = inverseCount(self.Q, x, y, z, alfa, beta)

        print(self.Q)
        self.pubAngles(self.Q)

    def goHome(self):
	self.Q = [0.11, 0.11, -0.11, 0.11, 0.11]
	print('going home')	
	self.pubAngles(self.Q)

    def goToCandle(self):
	self.Q = [2.95, 1.05, -2.44, 1.73, 2.95]
	print('going to candle pos')	
	self.pubAngles(self.Q)
        

    def info(self):
        print('')
        print('---------------------------')
        print('Please enter one of the following commands: ')
        print('     >>>goTo<<< to enter desired x, y and z')
        print('     >>>pick<<< to pick object in front of robot')
        print('     >>>place<<< to place object on the robot')
        print('     >>>home<<< to go to home position')
        print('     >>>candle<<< to go to candle position')
	print('     >>>direct<<< to calculate direct kinematics')
        print('     >>>Quit<<< to exit')
        print('')

    def __del__(self):
        print("Robot deleted")
