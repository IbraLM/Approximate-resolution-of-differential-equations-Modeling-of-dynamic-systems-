#!/usr/bin/python3.7

import numpy as np
import matplotlib.pyplot as plt
import methods as m
from math import *
from time import time

def equation_simple_pendulum(gravity=9.81, pendulum_length=1.0):
    """
    Computes the equation of the simple pendulum
    gravity         : The applied gravity (default value : 9.81m/s²)
    pendulum_length : The length of the pendulum (default value : 1m)
    """
    return lambda X, t : np.array([X[1], (-gravity/pendulum_length) * np.sin(X[0])])
    
def simple_pendulum_frequency(t0, tf, eps, theta):
    """
    Computes the frequency of the pendulum
    t0    : The beginning of the timer
    tf    : The ending of the timer
    eps   : The desired accuracy
    theta : The initial angle
    """
    y0 = np.array([theta, 0.0])
    t = time()
    result = m.meth_epsilon(y0, t0, tf, eps, equation_simple_pendulum() , m.step_RK4)
    n_var=0
    for i in range(1,len(result)-1):
        if (result[i,0]-result[i-1,0])*(result[i+1,0]-result[i,0])<0:
            n_var+=1
    return n_var/(2.*(tf-t0))
    

def display_frequency(t0, tf, eps, min_theta, max_theta):
    """
    Display the frequency according to a min and max theta
    t0        : The beginning of the timer
    tf        : The ending of the timer
    eps       : The desired accuracy
    min_theta : The first theta value computed
    max_theta : The last theta value computed
    """
    theta = np.arange(min_theta, max_theta, 5e-2)

    y = []
    print("Generating simple pendulum frequency acoording different θ values")
    for i in range(len(theta)):
        print(round(i/(float(len(theta)))*100, 1), "%", end="\r")
        y.append(simple_pendulum_frequency(t0, tf, eps, theta[i]))

    u = plt.plot(theta, y,label="frequence", linewidth=1.0)
    sgl=sqrt(9.81/1.0)*1/(2*pi)
    list=np.zeros(len(theta))
    for i in range(len(theta)):
        list[i]=sgl
    plt.plot(theta, list, color='red',label="sqrt(g/l)*1/(2*pi)", linewidth=1.0)
    plt.legend()
    plt.xlabel("Theta")
    plt.ylabel("Frequence")
    plt.show()
    
def solve_simple_pendulum_equation(t0, tf, eps, theta):
    """
    Resolve the simple pendulum equation
    t0    : The beginning of the timer
    tf    : The end of the timer
    eps   : The desired accuracy
    theta : The starting angle
    """
    y0 = np.array([theta, 0.0])
    y_theta = []
    y_omega = []
    res = m.meth_epsilon(y0, t0, tf, 1e-3, equation_simple_pendulum(5, 1), m.step_RK4)
    x = np.arange(t0, tf, (tf - t0)/len(res))
    for i in range(len(res)):
        y_theta.append(res[i][0])
        y_omega.append(res[i][1])

    return (x, y_theta, y_omega)

