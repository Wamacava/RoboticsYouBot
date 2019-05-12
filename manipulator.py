import numpy as np
import math
# Inverse Kinematics Code

# Link Length in centimeters
L1 = 14.7
L2 = 15.5
L3 = 13.5
L4 = 8.1
L5 = 13.7

def main():
    Q = InverseKinematics(1,1,1,2,3)
    print(Q)


 # given x, y, z, alfa, beta function will compute
 # angles of joint 1..5
def InverseKinematics(x, y, z, alfa, beta):
    Q = [1,1,1,1,1]  # array of joint angles

    xc, yc, zc = CountOc()

    ### Q0 ###

    Q[0] = np.arctan(yc/xc)

    ### Q1 and Q2 ###

    r = math.sqrt(xc^2+yc^2) - L1
    s = zc - L2

    D = (( r*r + s*s ) - L3*L3 - L4*L4 ) / (2 * L3 * L4)   # cos(Q3)

    D2 = 1 - D*D

    if D2 < 0 :
        Q[1] =0
        Q[2] =0
    else:
        Q[2] = np.arctan(math.sqrt(1 - D*D) / D)
        Q[1] = np.arctan(r / (zc - L2)) - np.arctan( (L4 *np.sin(Q[3]) ) / (L3 + L4*np.cos(Q[3])) )

    ### Q3 ###

    Q[3] = -Q[1] - Q[2] - beta - np.pi/2

    ### Q4 ###
    Q[4] = alfa   # i'm not sure about that


    #here we need to add code to check if any joint is not out of the range

    return Q


def CountOc():  #function to compute Oc, No idea how to do it

    xc =1
    yc =1
    zc =1

    return xc, yc, zc

if __name__=="__main__":
    main()
