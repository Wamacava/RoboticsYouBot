import numpy as np
import math
 # given x, y, z, alfa, beta function will compute
 # angles of joint 1..5

def inverseCount(Q, x, y, z, alfa, beta):
    L1 = 14.7
    L2 = 15.5
    L3 = 13.5
    L4 = 8.1
    L5 = 13.7
    #degrees to radians

    alfa = alfa * np.pi /180
    beta = beta * np.pi /180

    #Q = actual position                # probably we need to read Q from ros topic here

    #Q = [0, 0.3, -0.05, 0, -90]  # array of joint angles

    xc, yc, zc = countOc(Q,x,y,z)

    ### Q0 ###

    Q[0] = np.arctan(yc/xc)

    ### Q1 and Q2 ###

    r = math.sqrt(xc*xc+yc*xc) - L1
    s = zc - L2

    D = (( r*r + s*s ) - L3*L3 - L4*L4 ) / (2 * L3 * L4)   # cos(Q3)

    D2 = 1 - D*D

    if D2 < 0 :
        Q[0] =0
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


def countOc(Q, x, y, z):  #function to compute Oc, No idea how to do it
    L1 = 14.7
    L2 = 15.5
    L3 = 13.5
    L4 = 8.1
    L5 = 13.7

    r13 = math.cos(Q[0]) * math.sin(Q[1]+Q[2]+Q[3])
    r23 = math.sin(Q[0]) * math.sin(Q[1]+Q[2]+Q[3])
    r33 = math.cos(Q[1]+Q[2]+Q[3])

    xc = x - (L5) * r13
    yc = y - (L5) * r23
    zc = z - (L5) * r33

    return xc, yc, zc
