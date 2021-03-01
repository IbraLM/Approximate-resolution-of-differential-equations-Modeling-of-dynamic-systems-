import matplotlib.pyplot as plt
import numpy as np


def display_field(f, xmin, ymin, xmax, ymax, dx, dy):

    X = np.zeros([len(np.arange(xmin, xmax, dx)), 
                  len(np.arange(ymin, ymax, dy))])
    Y = np.copy(X)
    U = np.copy(X)
    V = np.copy(Y)
   
    for i in range(X.shape[0]): 
        for j in range(X.shape[1]): 
            X[i,j] = x0 + i*dx
            Y[i,j] = y0 + j*dy
            
            derivee = f([X[i,j],Y[i,j]], 0)
            U[i,j] = derivee[0]
            V[i,j] = derivee[1]


    
