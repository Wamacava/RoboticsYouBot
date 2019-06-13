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
    
    while True:
        inp = raw_input('>>>')
	inp = inp.lower()

        
        if inp == 'setangles':	  #####---SET ANGLES---######
            entered = raw_input('Enter >Q1 Q2 Q3 Q4 Q5 < position in degrees separated by space:      ')
            splited = entered.split()
	    print(splited)

            try:
                rob.Q[0] = (float(splited[0])  *math.pi) /180
                rob.Q[1] = (float(splited[1]) *math.pi) /180
                rob.Q[2] = (float(splited[2]) *math.pi) /180
                rob.Q[3] = (float(splited[3]) *math.pi) /180
                rob.Q[4] = (float(splited[4]) *math.pi) /180

                print("changed Q: ", rob.Q)
            
            except:
                print('Something went wrong, values incorect')
                rob.info()
                continue

            rob.pubAngles()
            print('Done')

	elif inp == 'direct':      #####---DIRECT---######
	    rob.directKinematics()

        elif inp == 'inverse':      #####---INVERSE---#####

            entered = raw_input('Enter >x y z plane(left right front back) phi(orientation of 4th joint w.r.t the horizontal plane) < separated by spaces. phi -90 means that we want end effector to be oriented to the ground      >>>')
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
                rob.info()
                continue


            try:
                rob.inverseKinematics(x, y, z, where, phi)

            except:
                print('Something went wrong, most probably point is unreachable(cos(theta3>1 or < -1))')
                rob.info()
                continue
        elif inp == 'home':	    #####---HOME---######
            rob.goHome()

        elif inp == 'candle':	    #####---CANDLE---######
            rob.goToCandle()

        elif inp == 'pick':	   #####---PICK---######
            print('ok')




        elif inp == 'goto':	   #####---GO TO---######
            entered = raw_input('Enter >x y z alfa beta< position separated by space: ')
            splited = entered.split()
            print(splited)
            try:
                x = float(splited[0]) 
                y = float(splited[1])

                z = float(splited[2])
                alfa =float(splited[3])
                beta = float(splited[4])
		
            except:
                print('Something went wrong, values incorect')
                rob.info()
                continue


            print('We should call inverseKinematics function in this place, ')
            print('In inverseKinematics function publish function')

	    print(x, y, z, alfa, beta)
            rob.inverseKinematics(x, y, z, alfa, beta)

            print('Done')


        elif inp == 'exit':        #####---exit---######
            print("See you!")
            quit()

        else:
            print('Command incorrect')

        rob.info()




if __name__=="__main__":
    main()
