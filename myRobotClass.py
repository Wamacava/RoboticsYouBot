#myRobot class contains methods necessary to perform pick and place operation
from inverse import inverseCount
import numpy as np
import math
import rospy
from talker import talker
from talkerGripper import talkerGripper
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
        self.G=[0.011, 0.011] ###open gripper
        talkerGripper(self.G)
	self.info()

    def directKinematics(self):

	x, y, z = directCount(self.Q)

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

        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

        time.sleep(2)


        try:
            talker([self.Q[0], 0, 0, 0, 0])  #avoiding destruction

        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

        time.sleep(2)

        try:
            talker(self.Q)

        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

        self.lastQ = self.Q
        time.sleep(1)

    def pubGripper(self):

        try:
            talkerGripper(self.G)
        except rospy.ROSInterruptException:
	    print("error during publishing")
            pass
        print('')

    def closeGripper(self):
        print('')



    def inverseKinematics(self, x, y, z, where,phi):

        self.Q = inverseCount(x, y, z, where,phi)
        self.pubAngles()



    def pick(self):

        dir = self.getdir()
        x, y, z, where, phi = self.getPoint(dir)
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(4)
        self.G=[0.0, 0.0]  ###close gripper
        talkerGripper(self.G)
        time.sleep(2)
        self.goToCandle()


    def place(self):
        dir = self.getdir()
        x, y, z, where, phi = self.getPoint(dir)
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(4)
        self.G=[0.011, 0.011] ###open gripper
        self.pubGripper()
        time.sleep(2)
        self.goToCandle()

    def pickplace(self):
        x, y, z, where, phi = self.getPoint('front')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(4)
        self.G=[0.0, 0.0]  ###close gripper
        self.pubGripper()
        time.sleep(2)

        x, y, z, where, phi = self.getPoint('backL')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(4)
        self.G=[0.011, 0.011] ###open gripper
        self.pubGripper()
        time.sleep(2)
        self.goToCandle()

    def demo(self):

        x, y, z, where, phi = self.getPoint('right')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(2)
        self.G=[0.0, 0.0]  ###close gripper
        self.pubGripper()
        time.sleep(2)

        x, y, z, where, phi = self.getPoint('backR')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(2)
        self.G=[0.011, 0.011] ###open gripper
        self.pubGripper()
        time.sleep(2)
        self.goToCandle()


        x, y, z, where, phi = self.getPoint('front')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(4)
        self.G=[0.0, 0.0]  ###close gripper
        self.pubGripper()
        time.sleep(2)

        x, y, z, where, phi = self.getPoint('backL')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(2)
        self.G=[0.011, 0.011] ###open gripper
        self.pubGripper()
        time.sleep(2)
        self.goToCandle()



        x, y, z, where, phi = self.getPoint('backR')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(2)
        self.G=[0.0, 0.0]  ###close gripper
        self.pubGripper()
        time.sleep(2)

        x, y, z, where, phi = self.getPoint('left')
        self.inverseKinematics(x, y, z, where,phi)
        time.sleep(2)
        self.G=[0.011, 0.011] ###open gripper
        self.pubGripper()
        time.sleep(2)

        self.goToCandle()

    def getPoint(self, dir):




        if dir == 'front':	  #####---FRONT---######

            x = -274
            y = 0
            z= -113
            where = dir
            phi = -math.pi/2
        elif dir == 'right':	  #####---RIGHT---######
            x = 0
            y = -274
            z=  -113
            where = dir
            phi = -math.pi/2
        elif dir == 'left':	  #####---left---######
            x = 0
            y =274
            z= -113
            where = dir
            phi = -math.pi/2
        elif dir == 'backR':	  #####---backR---######
            x = 280
            y = 0
            z= 50
            where = dir
            phi =  -math.pi/2

        elif dir == 'backL':	  #####---backL---######
            x = 280
            y = 0
            z= 50
            where = dir
            phi =  -math.pi/2

        else:
            print("wrong direction")
            x= 0
            y= 0
            z= 0
            where = b
            phi = 0
        return x, y, z, where, phi


    def getdir(self):
        print("Enter where you want to pick object")
        print("front left right backL backR")
        inp = raw_input('>>> ')
        return inp

    def info(self):
        print('')
        print('---------------------------')
        print('Please enter one of the following commands: ')
        print('     >>>direct<<< to calculate direct kinematics')
        print('     >>>inverse<<< to calculate inverse kinematics')
        print('     >>>setangles<<< to enter desired joint values')
        print('     >>>home<<< to go to home position')
        print('     >>>candle<<< to go to candle position')
        print('     >>>pick<<< to pick object in front of robot')
        print('     >>>place<<< to place object on the robot')
        print('     >>>pick&place<<< to place object on the robot')
        print('     >>>demo<<< demonstration of pick and place possibilities')
        print('     >>>exit<<< to exit')
        print('')

    def run(self):
        while True:
            inp = raw_input('>>>')
	    inp = inp.lower()


            if inp == 'setangles':	  #####---SET ANGLES---######
                entered = raw_input('Enter >Q1 Q2 Q3 Q4 Q5 < position in degrees separated by space:      ')
                splited = entered.split()
	        print(splited)

                try:
                    self.Q[0] = (float(splited[0])  *math.pi) /180
                    self.Q[1] = (float(splited[1]) *math.pi) /180
                    self.Q[2] = (float(splited[2]) *math.pi) /180
                    self.Q[3] = (float(splited[3]) *math.pi) /180
                    self.Q[4] = (float(splited[4]) *math.pi) /180

                    print("changed Q: ", self.Q)

                except:
                   print('Something went wrong, values incorect')
                   self.info()
                   continue

                self.pubAngles()
                print('Done')

	    elif inp == 'direct':      #####---DIRECT---######
	        self.directKinematics()

            elif inp == 'inverse':      #####---INVERSE---#####

               print("                 >>>Enter >x y z plane phi <<<")
               print(" ")
               print("plane is: left, right, front, backL, backR ")
               print(" ")

               print("phi is orientation of 4th joint w.r.t the horizontal plane . phi -90 means that we want end effector to be oriented to the ground")
               print(" ")
               entered = raw_input(">>>>>")
               splited = entered.split()
	       print(splited)


               try:
                   x = float(splited[0])
                   y = float(splited[1])
                   z = float(splited[2])
                   where = splited[3]
                   phi = (float(splited[4]) *math.pi) /180

                   print(x, y, z, where, phi)


               except:
                   print('Something went wrong, values incorect')
                   self.info()
                   continue


               try:
                   self.inverseKinematics(x, y, z, where, phi)

               except:
                   print('Something went wrong, most probably point is unreachable(cos(theta3>1 or < -1))')
                   self.info()
                   continue

            elif inp == 'home':	    #####---HOME---######
                self.goHome()

            elif inp == 'candle':	    #####---CANDLE---######
                self.goToCandle()

            elif inp == 'pick':	   #####---PICK---######
                self.pick()

            elif inp == 'place':	   #####---PLACE---######
                self.place()

            elif inp == 'pick&place':	#####---PICK&PLACE---######
                self.pickplace()

            elif inp == 'demo':	#####---DEMO---######
                self.demo()

            elif inp == 'exit':        #####---exit---######
                print("See you!")
                quit()

            else:
                print('Command incorrect')

            self.info()



    def __del__(self):
        print("Robot deleted")
