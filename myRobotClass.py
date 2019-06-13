#myRobot class contains methods necessary to perform pick and place operation
from inverse import inverseCount
import numpy as np
import math
import rospy
from talker import talker
from direct import directCount
import time

class myRobot:
    Q =  [-2.84, -0.94, 2.33, -1.62, -2.84]  # home pos
    lastQ =  [-2.84, -0.94, 2.33, -1.62, -2.84] 
    #Q = [0, 0, 0, 0, 0] #candle pos
    G= [0, 0] # gripper Left, Right

    # Link Length in centimeters:
    L1 = 14.7
    L2 = 15.5
    L3 = 13.5
    L4 = 8.1
    L5 = 13.7


    def __init__(self):

        print('Hello')
        self.goToCandle()
	self.info()

    def directKinematics(self):
	
	x, y, z = directCount(self.Q)

	print('x, y, z: ', x, y, z)

    def goHome(self):
	self.Q = [-2.84, -0.94, 2.33, -1.62, -2.84]
	print('going home')	
	self.pubAngles()


    def goToCandle(self):
	self.Q = [0, 0, 0, 0, 0]
	print('going to candle pos')	
	self.pubAngles()
  

    def pubAngles(self):


     
	

        try:
            talker([self.lastQ[0], 0, 0, 0, 0])  #going to candle position before every move
    	    print("done")                                         
        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

        time.sleep(1)


        try:
            talker([self.Q[0], 0, 0, 0, 0])  #avoiding destruction
    	    print("done")                                         
        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

        time.sleep(1)



        try:
            talker(self.Q)
    	    print("done")
        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

        self.lastQ = self.Q

    def pubGripper(self, G):
        print('')


    def closeGripper(self):
        print('')


    def inverseKinematics(self, x, y, z, where,phi):

        self.Q = inverseCount(x, y, z, where,phi)
        
        print("Counted values of angles: ", self.Q)
        self.pubAngles()



    def info(self):
        print('')
        print('---------------------------')
        print('Please enter one of the following commands: ')
        print('     >>>direct<<< to calculate direct kinematics')
        print('     >>>inverse<<< to calculate inverse kinematics')
        print('     >>>goTo<<< to enter desired x, y and z')
        print('     >>>setangles<<< to enter desired joint values')
        print('     >>>home<<< to go to home position')
        print('     >>>candle<<< to go to candle position')
        print('     >>>pick<<< to pick object in front of robot')
        print('     >>>place<<< to place object on the robot')
        print('     >>>exit<<< to exit')
        print('')

    def __del__(self):
        print("Robot deleted")
