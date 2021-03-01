#!/usr/bin/python3.7

import unittest
import methods as m
from math import *
import numpy as np
import matplotlib.pyplot as plt
from time import time


def f1(x):
    return np.array([exp(atan(x))])

def dim1(y,t):
    return np.array([y/(1.+t**2)])

def f2(x):
    return np.array([cos(x),sin(x)])

def dim2(y,t):
    return np.array([-y[1], y[0]])

class TestMethods(unittest.TestCase):

    #Tests dimension 1

    def test_dim1(self):
        N = 100

        ti=time()
        X=np.linspace(0,10,N)
        Y=np.zeros(N)
        print(time()-ti)
        for i in range(N):
            Y[i]=f1(X[i])
            
        print(time()-ti)

        Y1 = m.meth_epsilon(f1(0), 0, 10, e-2, dim1, m.step_euler)
        Y2 = m.meth_epsilon(f1(0), 0, 10, e-2, dim1, m.step_RK4)
        Y3 = m.meth_epsilon(f1(0), 0, 10, e-2, dim1, m.step_middle_point)
        Y4 = m.meth_epsilon(f1(0), 0, 10, e-2, dim1, m.step_heun)
        
        print(time()-ti)
        
        X1=np.linspace(0,10,len(Y1))
        X2=np.linspace(0,10,len(Y2))
        X3=np.linspace(0,10,len(Y3))
        X4=np.linspace(0,10,len(Y4))
        
        plt.plot(X, Y, color="black", label="expected function")
        plt.plot(X1, Y1, color="red", label="Eulers method")
        plt.plot(X2, Y2, color="green", label="RK4 method")
        plt.plot(X3, Y3, color="blue", label="Middles points method")
        plt.plot(X4, Y4, color="orange", label="Heun method")
        plt.legend()
        plt.show()
        print(time()-ti)

    def test_dim2(self):
        N = 100
        ti=time()
        X=np.linspace(0,10,N)
        Y=np.zeros((N,2))
        print(time()-ti)
        for i in range(N):
            Y[i]=f2(X[i])
            
        print(time()-ti)
        
        Y1 = m.meth_epsilon(f2(0), 0, 10, 1e-2, dim2, m.step_euler)
        Y2 = m.meth_epsilon(f2(0), 0, 10, 1e-2, dim2, m.step_RK4)
        Y3 = m.meth_epsilon(f2(0), 0, 10, 1e-2, dim2, m.step_middle_point)
        Y4 = m.meth_epsilon(f2(0), 0, 10, 1e-2, dim2, m.step_heun)
        
        print(time()-ti)
        
        X1=np.linspace(0,10,len(Y1))
        X2=np.linspace(0,10,len(Y2))
        X3=np.linspace(0,10,len(Y3))
        X4=np.linspace(0,10,len(Y4))
        
        plt.plot(Y[:,0], Y[:,1], color="black", label="expected function")
        plt.plot(Y1[:,0], Y1[:,1], color="red", label="Eulers method")
        plt.plot(Y2[:,0], Y2[:,1], color="green", label="RK4 method")
        plt.plot(Y3[:,0], Y3[:,1], color="blue", label="Middles points method")
        plt.plot(Y4[:,0], Y4[:,1], color="orange", label="Heun method")

        x = np.arange(-1, 1, 0.05)
        y = np.arange(-1, 1, 0.05)

        X, Y = np.meshgrid(x, y)
        result = dim2(np.array([X, Y]),0)
        n = 0
        color_array = np.sqrt(((result[1]-n)/2)**2 + ((result[0]-n)/2)**2)
        plt.quiver(X,Y,result[0],result[1], color_array, alpha = 1)


        plt.axis([-1, 1, -1, 1])
        plt.legend()
        plt.show()
        print(time()-ti)
    
if __name__ == '__main__':
    unittest.main()
