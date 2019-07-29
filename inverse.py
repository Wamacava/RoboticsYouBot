


import numpy as np
import math
from numpy import array

 # given x, y, z, alfa and plane
 # angles of joint 1..5

def inverseCount(x,y,z,where,phi):


    print("")
    print("-----------------------------------------------")
    print("")
    print("Inverse kinematics result:")
    print("Got values")
    print("x= ", x, "y= ", y, "z= ", z, "where= ", where)
    print("deviation of the 4th joint w.r.t horizontal plane: ", phi*180 / math.pi)
    print("")


    L1 = 147
    L2 = 155
    L3 = 135
    L45 = 218
    Q = [0,0,0,0,0]


    x = math.sqrt(x*x+y*y) #distance from center of manipulator to the poin
			   #transformation from global coordinate system to
                           #coordinate system of planar manipulator

    x = x - 33            #setting base of planar manipulator into joint 2 on x axis
    z = z - L1            #setting base of planar manipulator into joint 2 on z axis




    if (where == "front"):
        Q[0]= 0 #like in candle


    elif(where == "backR"):
        Q[0]= 2.88 # place right


    elif(where == "backL"):
        Q[0]= -2.88 # place left



    elif(where== "right"):
        Q[0]= math.pi/2 #candle
    elif (where== "left"):
        Q[0]= -math.pi/2

    else:
        print("Error!")

    X4= x -(L45)*math.cos(phi)  #(A4+A5) fourth and fifth links are considered an unique EE link, due to the same local axis
    Z4= z -(L45)*math.sin(phi)


    C3= (X4*X4+Z4*Z4-L2*L2-L3*L3)/(2*L2*L3)  #C3 is cos(theta3)


    S3= -(math.sqrt(1-(C3*C3)))
    Q[2]=math.atan2(S3,C3)

    C2= (((L2+(L3*C3))*Z4)-(L3*S3*X4))/((X4*X4)+(Z4*Z4))
    S2= (((L2+(L3*C3))*X4)+(L3*S3*Z4))/((X4*X4)+(Z4*Z4))
    Q[1]=math.atan2(S2,C2)



    Q[1] = math.pi/2 - Q[1]    #planar manip equations count 0 as horozontal plane, youbot as candle position

    Q[3]= phi - Q[2] - Q[1]


 #   Q[2]= -Q[2]
 #   Q[3]= -phi - Q[2] - Q[1]  # maybe - - Q2



#    Q[3]= -Q[3]  #because youbot arms move other way than standard manipulator

    Q[4]=0


    Q[1] = math.pi/2 - Q[1]
    Q[2] = -Q[2]
    Q[3]= -Q[3]



    print("Result:")

    print(Q[0]*180 / math.pi, Q[1]*180 / math.pi, Q[2]*180 / math.pi, Q[3]*180 / math.pi, Q[4]*180 / math.pi)


    print("-----------------------------------------------")
    print("")

    return Q


#inverseCount(431, 0, 103, "front", -math.pi/4)


#inverseCount(0, 274, -113, "left", -math.pi/2) #-90 70 65 45 0    PICK LEFT
#inverseCount(0, -274, -113, "right", -math.pi/2) #90 70 65 45 0    PICK RIGHT
#inverseCount(-274, 0, -113, "front", -math.pi/2) #0 70 65 45 0    PICK FRONT

#inverseCount(280, 0, 50, "backR", -math.pi/2) # # 165 47 37 96 0  #  GOOD PLACE RIGHT

#inverseCount(280, 0, 50, "backL", -math.pi/2) # # -165 47 37 96 0  #  GOOD PLACE LEFT




#inverseCount(0, -365, 103, "left", -math.pi/4)

#inverseCount(274, 431, 103, "left", -math.pi/4)   # 45x3 left

#inverseCount(0, 455, 352, "left", 0)  # 0 45 0 45 0
