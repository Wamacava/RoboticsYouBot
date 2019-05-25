import numpy as np
import math
###import rospy
###from brics_actuator.msg import JointPositions, JointValue, Poison
from myRobotClass import myRobot
###from talker import talker



def main():
    rob = myRobot()

    rob.info()

    while True:
        inp = input('>>>')

        if inp == 'goTo':
            entered = input('Enter >x y z alfa beta< position separated by space: ')
            splited = entered.split(' ')

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

            rob.inverseKinematics(x, y, z, alfa, beta)

            print('Done')

        elif inp == 'home':
            rob.goHome()

        elif inp == 'candle':
            rob.goToCandle()

        elif inp == 'pick':
            print('ok')

        elif inp == 'candle':
            print('ok')

        elif inp == 'Quit':
            print("See you!")
            quit()

        else:
            print('Command incorrect')

        rob.info()
#    Q = InverseKinematics(-0.1, 0.3, -0.05, 0, -80, 0.01)
#    print(Q)



if __name__=="__main__":
    main()
