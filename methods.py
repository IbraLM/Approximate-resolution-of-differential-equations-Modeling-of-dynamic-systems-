#!/usr/bin/python3.7
import numpy as np
from math import *

def meth_n_step(y0, t0, N, h, f, step_method):
    """
    Given a point (t0, y0), this function computes an N
    number of steps (evenly distributed), of size h, using the right
    method, for the Cauchy problem, with y(t0) = y0, and 
    y'' = f(y).
    y0          :
    t0          : The beginning of the timer
    N           : The number of steps.
    f           : The function computed.
    step_method : The used method.
    """
    y = y0
    t = t0
    result = np.zeros((N,len(y0)))
    for step in range(N):
        y = step_method(y, t, h, f)
        t = t + h
        result[step] = y
    return result


def diff_infinite_norm(first_value, second_value):
    """ 
    Computes the infinite norm of (first_value - second_value)
    first_value  : The first vector
    second_value : The second vector
    """
    return np.linalg.norm(first_value-second_value[::2, :], np.inf)


def meth_epsilon(y0, t0, tf, eps, f, step_method):
    """
    Return the array solving the Cauchy problem.
    y(t0) = y0, y' = f(y).
    Values are evenly distributed on [t0, tf].
    y0          : The differential equation system
    t0          : The beginning of the timer
    tf          : The ending of the timer
    eps         : The desired accuracy.
    f           : The function computed.
    step_method : The used method.
    """
    N = 400
    result_N = meth_n_step(y0, t0, N, float((tf-t0))/float(N), f, step_method)
    N *= 2
    result_2N = meth_n_step(y0, t0, N, float((tf-t0))/float(N), f, step_method)
    i=0
    while ((diff_infinite_norm(np.copy(result_N), np.copy(result_2N)) > eps) and (i<10**9)):
        result_N = np.copy(result_2N)
        N *= 2
        h = (tf - t0) / N
        result_2N = meth_n_step(y0, t0, N, h, f, step_method)
        i+=1
    return result_2N

    
def step_euler(y, t, h, f):
    """
    Compute the step with Euler's method.
    y : The 
    t : The current time
    h : The step
    f : The computed function
    """
    return (y + h * f(y, t))

def step_middle_point(y, t, h, f):
    """
    Compute the step with the method of middles points.
    y :
    t : The current time
    h : The step
    f : The computed function
    """
    y_middle = y + (h / 2.) * f(y, t)
    pn = f(y_middle, t + (h / 2.))
    return (y + h * pn)

def step_heun(y, t, h, f):
    """
    Compute the step with Heun's method.
    y :
    t : The current time
    h : The step
    f : The computed function
    """
    pn1 = f(y, t)
    y2 = y + h * pn1
    pn2 = f(y2, t + h) 
    return (y + h * (pn1 + pn2) / 2.)

def step_RK4(y, t, h, f):
    """
    Compute the step with the fourth order Runge-Kutta's method.
    y :
    t : The current time
    h : The step
    f : The computed function
    """
    pn1 = f(y, t)
    y2 = y + (1. / 2.) * h * pn1
    pn2 = f(y2, t + (1. / 2.) * h)
    y3 = y + (1. / 2.) * h * pn2
    pn3 = f(y3, t + (1. / 2.) * h)
    y4 = y + h * pn3
    pn4 = f(y4, t + h)
    return (y + (1./6.) * h * (pn1 + 2 * pn2 + 2 * pn3 + pn4))
