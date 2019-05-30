import numpy as np
import math
from numpy import array

def ScrewZ(q,d):
    c1 = math.cos(q)
    s1 = math.sin(q)
    Z = array([
    [c1,-s1,0, 0],
    [s1,c1,0, 0],
    [0,0,1,d],
    [0,0,0,1], ])
    return Z

def ScrewX(alfa,a):
    c1 = math.cos(alfa)
    s1 = math.sin(alfa)
    X = array([
    [1,0,0, a],
    [0,c1,-s1, 0],
    [0,s1,c1,0],
    [0,0,0,1], ])
    return X


def directCount(Q):

    Q[0] -= 2.9150354
    Q[1] -= 1.0958636
    Q[2] += 2.5481815 
    Q[3] -= 1.7247770
    Q[4] -= 2.8761045
    Q = [0,0,0,0,0]
    L1 = 14.7
    L2 = 15.5
    L3 = 13.5
    L4 = 8.1
    L5 = 13.7  #L5+L6
    pm = (math.pi)/2
    T00 = array([
    [1,0,0, 0],
    [0,1,0, 0],
    [0,0,1, 0],
    [0,0,0, 1], ])
    #Finding the homogeneous transformation of the system
    
    #T01 = np.dot(T00,np.dot(ScrewZ(Q[0],L2),ScrewX(-pm,L1)))
    T01 = np.matmul(np.matmul(T00,ScrewZ(Q[0],L2)),ScrewX(-pm,L1))
    T02 = np.dot(T01,np.dot(ScrewZ(Q[1],0),ScrewX(0,L3)))
    T03 = np.dot(T02,np.dot(ScrewZ(Q[2],0),ScrewX(0,L4)))
    T04 = np.dot(T03,np.dot(ScrewZ(Q[3],0),ScrewX(pm,0)))
    T05 = np.dot(T04,np.dot(ScrewZ(Q[4],L5),ScrewX(0,0)))
    
    
    

   
    #T02 = np.matmul(np.matmul(T01,ScrewZ(Q[1],0)),ScrewX(0,L3))
    #T03 = np.matmul(np.matmul(T02,ScrewZ(Q[2],0)),ScrewX(0,L4))
    #T04 = np.matmul(np.matmul(T03,ScrewZ(Q[3],0)),ScrewX(pm,0))
    #T05 = np.matmul(np.matmul(T04,ScrewZ(Q[4],L5)),ScrewX(0,0))


    x = T05[0,3]
    y = T05[1,3]
    z = T05[2,3]

 
    print(T05)
    return x, y, z

