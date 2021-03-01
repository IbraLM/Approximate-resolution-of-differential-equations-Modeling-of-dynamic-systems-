#!/usr/bin/python3.7

import numpy as np
import matplotlib.pyplot as plt
import methods as m
from math import *


def equation_double_pendulum(m1=1, m2=1, l1=1, l2=1, gravity=9.81):
    """
    Computes  equations of the double pendulum
    gravity  : The applied gravity (default value : 9.81m/s²)
    l1       : The length of the first link (default value : 1m)
    l2       : The length of the second link (default value : 1m)
    m1       : The mass of the first link (default value : 1kg)
    m2       : The mass of the second link (default value : 1kg)
    """
    
    def f(X, t):
        theta_1 = X[0]
        omega_1 = X[1] # omega_1 = theta_1'
        theta_2 = X[2]
        omega_2 = X[3] # omega_2 = theta_2'
        return np.array([omega_1,
                         (-gravity*(2*m1+m2)*np.sin(theta_1)-m2*gravity*np.sin(theta_1-2*theta_2) \
                          -2*np.sin(theta_1-theta_2)*m2*(l2*omega_2**2+l1*np.cos(theta_1-theta_2)*omega_1**2)) \
                         /(l1*(2*m1+m2-m2*np.cos(2*theta_1-2*theta_2))),
                         omega_2,
                         (2*np.sin(theta_1-theta_2)*((m1+m2)*l1*omega_1**2+gravity*(m1+m2)*np.cos(theta_1) \
                                                     +l2*m2*np.cos(theta_1-theta_2)*omega_2**2)) \
                         /(l2*(2*m1+m2-m2*np.cos(2*theta_1-2*theta_2)))])
    return f
        


def display_double_pendulum_path(result, l1, l2, label):
    """
    Display the path double pendulum.
    result : The array containing the resolution of the movement equations.
    l1     : The length of the first link
    l2     : The length of the second link
    label  : The label of the curve
    """
    theta_1 = []
    theta_2 = []
    x = []
    y = []
    
    for i in range(len(result)):
        theta_1 = theta_1 + [result[i][0]]
        theta_2 = theta_2 + [result[i][2]]
        y = y + [-l1*np.cos(theta_1[i])-l2*np.cos(theta_2[i])]
        x = x + [l1*np.sin(theta_1[i])-l2*np.sin(theta_2[i])]
        
    plt.plot(x, y, linewidth=1.0, label=label)


def solve_double_pendulum_equation(t0, tf, y0, f, l1, l2):
    """
    Computes the trajectory of the end of the double pendulum as a function
    of time.
    t0 : The beginning of the timer
    y0 : 
    f  : The used function
    l1 : The length of the first link
    l2 : The length of the second link
    """
    result_1 = m.meth_epsilon(y0, t0, tf, 1e-1, f, m.step_RK4)
    result_2 = m.meth_epsilon(y0+np.array([0.1, 0.0, 0.0, 0.0]), t0, tf, 1e-1, f, m.step_RK4)
    result_3 = m.meth_epsilon(y0+np.array([0.0, 0.0, 0.1, 0.0]), t0, tf, 1e-1, f, m.step_RK4)


    display_double_pendulum_path(result_1, l1, l2, 'initial conditions (IC)')
    display_double_pendulum_path(result_2, l1, l2, 'θ1 = θ1(IC)+0.1')
    display_double_pendulum_path(result_3, l1, l2, 'θ2 = θ2(IC)+0.1')

    plt.legend()
    plt.title("Trajectoire de l'extrémité du double pendule en fonction du temps.")
    plt.show()


def turnaround_time(results):
    """
    Computes the turnaround time according to a given curve.
    results : the obtain curve according to initials condition.
    """
    i = 1
    while(i < len(results)-1 and (abs(results[i][0]) < np.pi and abs(results[i][2])<np.pi)): # If theta1 or theta2 > pi, then there is a tuen over. 
        i = i+1
    return i


def display_time(n_max):
    """
    Graph of the time taken by the double pendulum to turn over.
    n_max : The resolution of the map.
    """
    t0 = 0.0
    time_max = 10.0
    x = np.arange(0.0,time_max+time_max/n_max,time_max/n_max)
    array = np.zeros([n_max,n_max])
    u = (2*np.pi)/array.shape[0]
    v = -np.pi
    print("Generating the time map...")
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            print(round((i*array.shape[1]+j)/(float(array.shape[0]*array.shape[1]))*100, 2),"%", end="\r") #Loading time
            y0 = np.array([i*u+v, 0.0, j*u+v, 0.0]) # Allows to fluctuate between -pi and pi for theta1 and theta2
            result = m.meth_n_step(y0, t0, n_max, 10.0/n_max, equation_double_pendulum(2, 1, 1, 1, 9.81), m.step_RK4)
            time = turnaround_time(result)
            if(time == len(x)-1):
                array[i][j] = x[0] #If all the points of the curves have been run through then there is no turn over.
            else:
                array[i][j] = x[turnaround_time(result)]
    plt.pcolormesh(array, cmap = plt.cm.gist_stern, shading="gouraud")
    plt.title("Carte du temps du premier basculement du \npendule en fonction des conditions initiales")
    plt.clim()
    plt.colorbar()
    plt.show()
