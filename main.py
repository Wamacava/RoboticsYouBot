import numpy as np
import math
import rospy
from brics_actuator.msg import JointPositions, JointValue, Poison
from myRobotClass import myRobot
from talker import talker
import string





def main():
    rob = myRobot()

    rob.info()

    #rob.goToCandle()


    while True:
        inp = raw_input('>>>')
	inp = inp.lower()

        if inp == 'goto':
            entered = raw_input('Enter >x y z alfa beta< position separated by space: ')
            splited = entered.split()

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

        elif inp == 'home':
            rob.goHome()

        elif inp == 'candle':
            rob.goToCandle()

        elif inp == 'pick':
            print('ok')

	elif inp == 'direct':
	    rob.directKinematics()

        elif inp == 'quit':
            print("See you!")
            quit()

        else:
            print('Command incorrect')

        rob.info()




if __name__=="__main__":
    main()
