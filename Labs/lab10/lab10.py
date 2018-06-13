import random
import time
import test_driver

""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""

L1 = [ 15.1, -12.1,  5.4, 11.8, 17.4, 4.3, 6.9 ]

#L2 = [2.3, 4.5, 13.6, 11.8, 6.9, 10.0, -3.5]


def closest1(floats):
    '''
    >>> print(closest1 ([ 15.1, -12.1,  5.4, 11.8, 17.4, 4.3, 6.9 ] ))
    (5.4, 4.3)
    >>> print(closest1 ( [5] ))
    (None, None)
    >>> print(closest1( [2.3, 4.5, 13.6, 11.8,11.9, 10.0, -3.5] ))
    (11.8, 11.9)
    
    '''
    smallI = 0
    smallJ = 0
    if len(floats) < 2:
            return (None, None) 
    minDif = floats[0]-floats[1]
   
    for i in range(len(floats)):
        for j in range(i + 1, len(floats)):    
            dif = floats[i] - floats[j]
            if abs(dif) <= abs(minDif):
                minDif = dif
                smallI = floats[i]
                smallJ = floats[j]
   
    return (smallI, smallJ)
  

def closest2(floats):
    '''
    >>> print(closest2 ([ 15.1, -12.1,  5.4, 11.8, 17.4, 4.3, 6.9 ] ))
    (4.3, 5.4)
    >>> print(closest2 ( [5] ))
    (None, None)
    >>> print(closest2( [2.3, 4.5, 13.6, 11.8, 11.9, 10.0, -3.5] ))
    (11.8, 11.9)
    '''
    compare = []
    small1 = 0
    small2 = 0
    if len(floats) < 2:
        return (None, None)     
    compare = sorted(floats.copy())
    minDif = compare[0]-compare[1]
    for i in range(1, len(compare)-1):
        dif = compare[i+1]-compare[i]
        if abs(dif) <= abs(minDif):
            minDif = dif
            small1 = compare[i]
            small2 = compare[i+1]
            
    return (small1, small2)
    
if __name__ == "__main__":
    
    #(x, y) = closest1(L1)
    #print(x, y)
    
    #(x, y) = closest2(L1)
    #print(x, y)
    
    Lcheck = []
   
    i = 0
    while i < 1000:
        n = random.uniform(0.0, 1000.0)
        Lcheck.append(n)
        i += 1
    
    s1 = time.time()
    (i0,i1) = closest1(Lcheck)
    t1 = time.time() - s1
    print("Ver 1: time {:.3f} seconds".format(t1))
    
    s2 = time.time()
    (j0,j1) = closest2(Lcheck)
    t2 = time.time() - s2
    print("Ver 2: time {:.3f} seconds".format(t2))