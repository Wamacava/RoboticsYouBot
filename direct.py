import numpy as np
import math
from numpy import array


def directCount(Q):
    L1 = 14.7
    L2 = 15.5
    L3 = 13.5
    L4 = 8.1
    L5 = 13.7  #L5+L6
    T00 = array([
    [1,0,0, 0],
    [0,1,0, 0],
    [0,0,1, 0],
    [0,0,0, 1], ])



    x = 0
    y = 0
    z = 0

    print(T00)
    print(x,y,z)
    return x, y, z

Q = [0,0,0,0,0]
directCount(Q)
