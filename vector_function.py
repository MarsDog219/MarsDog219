
import numpy as np

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here

    if x <= y:
        func = np.dot(x,y)
        return func
    else:
        func = x/y    
        return func
           

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    #Your code here
    vfunc = np.vectorize(scalar_function(x,y))
    return vfunc

    
if __name__ == '__main__': 
    D = vector_function(2,5)
    print(D)
