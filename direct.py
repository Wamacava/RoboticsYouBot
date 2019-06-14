import numpy as np
import math
from numpy import array

def T(alfa,a,d,q):
    ct = math.cos(q)
    st = math.sin(q)
    ca = math.cos(alfa)
    sa = math.sin(alfa)

    T = array([
    [ct,-st*ca,st*sa,a*ct],
    [st,ct*ca,-ct*sa,a*st],
    [0,sa,ca,d],
    [0,0,0,1], ])
    return T

def directCount(Q):
    
    print("")

    print("Q in direct function: ", Q[0]*180 / math.pi, Q[1]*180 / math.pi, Q[2]*180 / math.pi, Q[3]*180 / math.pi, Q[4]*180 / math.pi)


    offset = (math.pi)/2
    L1 = 33
    L2 = 147
    L3 = 155
    L4 = 135
    L5 = 217.5 #L5+

    T00 = array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],])
    #Finding the homogeneous transformation of the system

    T0= np.matmul(T00,T(offset,33,147,-Q[0]))
    T1= np.matmul(T0,T(0,155,0,offset-Q[1]))
    T2=np.matmul(T1,T(0,135,0,-Q[2]))
    T3=np.matmul(T2,T(offset,0,0,offset-Q[3]))
    T4= np.matmul(T3,T(0,0,217.5,-Q[4]))
    x = T4[0,3]
    y = T4[1,3]
    z = T4[2,3]

    print("")
    print("Actual possition of the end effector (x, y, z): ")
    print(x, y ,z)
    print("")
    return x, y, z


