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

    Q[0] = math.atan2(yc,xc)

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
        Q[2] = math.atan2(math.sqrt(1 - D*D) , D)
        Q[1] = math.atan2(r , (zc - L2)) - math.atan2( (L4 *np.sin(Q[3]) ) , (L3 + L4*np.cos(Q[3])) )

    ### Q3 ###

    Q[3] = -Q[1] - Q[2] - beta - np.pi/2

    ### Q4 ###
    Q[4] = alfa   # i'm not sure about that
	

    #here we need to add code to check if any joint is not out of the range

    if(Q[0] == 0 and  Q[1] == 0 and Q[2] == 0 and Q[3] == 0 and Q[4] == 0):
	Q= [0.11, 0.11, -0.11, 0.11, 0.11062]
	print('all zeros')
	return Q


    print('-----------------------')
    print('Calculated values')
    print(Q)
    print('-----------------------')
    Q[0] += 2.9150354
    Q[1] += 1.0958636
    Q[2] -= 2.5481815 
    Q[3] += 1.7247770
    Q[4] += 2.8761045



    if(  Q[0] > 5.84014 or Q[0] < 0.0100692 or Q[1] < 0.0100692 or Q[1] > 2.61799 or Q[2] < -5.02655 or Q[2]>         -0.015708 or Q[3] > 3.4292 or Q[3] < 0.0221239 or Q[4] < 0.110619 or Q[4] > 5.64159):

	Q= [0.11, 0.11, -0.11, 0.11, 0.11062]
	print('Out of range, I go home')
 
    	

#    if(  Q[0] > 5.84014 or Q[0] < 0.0100692 or Q[1] < 0.0100692 or Q[1] > 2.61799 or Q[2] < -5.02655 or Q[2]> -0.015708 or Q[3] > 3.4292 or Q[3] < 0.0221239 or Q[4] < 0.110619  or Q[4] > 5.64159):
#	Q= [0.11, 0.11, -0.11, 0.11, 0.11]
#	print('Out of range, I go home')
	
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
