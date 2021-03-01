#!/usr/bin/python3.7

import unittest
from simple_pendulum import *
from double_pendulum import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
from time import time

class TestSimplePendulum(unittest.TestCase):
    
    def test_solve_simple_pendulum_equation(self):
        """
        Tests the variation of θ as function of time 
        for the simple pendulum.
        """
        theta = np.pi/2
        t0 = 0.0
        tf = 10.0
        eps = 1e-1
        (x, y_theta, y_omega) = solve_simple_pendulum_equation(t0, tf, eps, theta)

        x_arr = [-1, 11]
        y_pi = [-np.pi/2, -np.pi/2]
        y_pi2 = [np.pi/2, np.pi/2]
        plt.plot(x, y_theta, linewidth=1.0, label = "Theta")
        plt.plot(x_arr, y_pi, linewidth=1.0, label = "-pi/2", color = 'red')
        plt.plot(x_arr, y_pi2, linewidth=1.0, label = "pi/2", color = 'orange')
        plt.title("Variation de l'angle θ en fonction du temps")
        plt.legend()
        plt.show()

    def test_simple_pendulum_frequency(self):
        """
        Tests the frequency of the simple pendulum 
        and check that the frequency approaches sqrt(g/l)*1/2pi for weak oscillations.
        (We have to obtain a parabola).
        """
        t0 = 0.0
        tf = 400.0
        eps = e-2
        min_theta = -2
        max_theta = 2
        display_frequency(t0, tf, eps, min_theta, max_theta)
        

        
    def test_solve_double_pendulum_equation(self):
        """
        Display the trajectory of the end of the double pendulum as a function
        """
        l1 = 1
        l2 = 1
        m1 = 1
        m2 = 1
        t0 = 0.
        tf = 10.
        gravity = 9.81
        solve_double_pendulum_equation(t0, tf, [np.pi/4, 0, 2*np.pi/3, 0], equation_double_pendulum(l1, l2, m1, m2, gravity), l1, l2)

        
    def test_time_map(self):
        """
        Graph of the time taken by the double pendulum to turn over.
        """
        n_max = 100
        display_time(n_max)
    
if __name__ == '__main__':
    unittest.main()
