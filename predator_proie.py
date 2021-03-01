import numpy as np
import math
import matplotlib.pyplot as plt
from methods import * 


def subdivision(t0, tf, N) :
    dt = ( tf - t0 ) / ( N-1 )
    sub = np.zeros(N)
    for i in range(N):
        sub[i] = t0 + dt * i
    return sub


def malthusiens(nb_init, t0, tf, eps, methode, gamma ) :
    """
    Return  the array solving the Malthus model
    nb_init     : number of person in t0    
    t0          : The beginning of the timer
    tf          : The ending of the timer
    eps         : The desired accuracy.
    gamma       : proportionality coefficient
    """

    f=lambda y, t : gamma*y
    Y=meth_epsilon(nb_init, t0, tf, eps, f, methode)
    return Y
    

def verhulst(nb_init, t0, tf, eps, methode, gamma, K) :

     """
    Return  the array solving the Verhulst model
    nb_init     : number of person in t0    
    t0          : The beginning of the timer
    tf          : The ending of the timer
    eps         : The desired accuracy.
    gamma       : proportionality coefficient
     K          : Maximum capacity 
    """
     f=lambda y,t : gamma*y*(1-y/K)
     Y=meth_epsilon(nb_init, t0, tf, eps, f, methode)
     return Y


def eq_Lotka_Volterra(a, b, c, d):
    """
    Return the function of the model of Lotka Volterra
    """
    return lambda y, t : np.array([ y[0] * ( a - b * y[1]),\
                                    y[1] * ( c * y[0] - d)])


def Lotka_Volterra(a, b, c, d, init, t0, tf, eps):
     """
    Return  the array solving the Malthus model
    nb_init     : number of person in t0    
    t0          : The beginning of the timer
    tf          : The ending of the timer
    eps         : The desired accuracy.
    
    """

    
     Y=meth_epsilon(init, t0, tf, eps,\
                                  eq_Lotka_Volterra(a, b, c, d)  , step_RK4)
     return Y

def periode(y, t0, tf):
    """
    Return approximate period of the array y between t0 and tf

    """

    
    l=len(y)
    subd = subdivision(t0, tf, l)
    nb_periodes = 0
    m = 0
    periode_f = 0
    i = 1
    while (i < l):
        while ((i < l) and (y[i-1] > y[i])):
            i += 1
        while((i < l) and (y[i-1] < y[i])):
            i += 1
        if (i < l):
            if (nb_periodes == 0):
                m = subd[i-1]
            periode_f = subd[i-1]
            nb_periodes += 1

    if (nb_periodes < 2):
        print("Erreur")
        return 0
    else:
        return (periode_f-m)/(nb_periodes-1)

    
