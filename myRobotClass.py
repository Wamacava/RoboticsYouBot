#myRobot class contains methods necessary to perform pick and place operation

class myRobot:
    Q = [0, 0, 0, 0, 0]  # init values ???
    G= [0, 0] # gripper Left, Right
    def __init__(self):

        print('Hello')
        #?

    def pubAngles(self, Q):

        print('')

    def pubGripper(self, G):
        print('')


    def closeGripper(self):
        print('')


    def inverseKinematics(self, x, y, z, alfa, beta):

        print('')

    def goHome(self):

        print('goint to home pos')

    def goToCandle(self):
        print('goint to candle pos')

    def info(self):
        print('Please enter one of the following commands:s')
        print('')
        print('goTo to enter desired x, y and z')
        print('home to go to home position')
        print('candle to go to candle position')
        print('Quit to exit')

    def __del__(self):
        print("Robot deleted")
