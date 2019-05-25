#myRobot class contains methods necessary to perform pick and place operation
from inverse import inverseCount
import numpy as np
import math


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

        #try:
            #talker()
    	    #print("done")
        #except rospy.ROSInterruptException:
            #pass
        print('')

    def pubGripper(self, G):
        print('')


    def closeGripper(self):
        print('')


    def inverseKinematics(self, x, y, z, alfa, beta):

        self.Q = inverseCount(self.Q, x, y, z, alfa, beta)

        print(self.Q)
        self.pubAngles(self.Q)

    def goHome(self):

        print('goint to home pos')

    def goToCandle(self):
        print('goint to candle pos')

    def info(self):
        print('')
        print('---------------------------')
        print('Please enter one of the following commands: ')
        print('     >>>goTo<<< to enter desired x, y and z')
        print('     >>>pick<<< to pick object in front of robot')
        print('     >>>place<<< to place object on the robot')
        print('     >>>home<<< to go to home position')
        print('     >>>candle<<< to go to candle position')
        print('     >>>Quit<<< to exit')
        print('')

    def __del__(self):
        print("Robot deleted")
