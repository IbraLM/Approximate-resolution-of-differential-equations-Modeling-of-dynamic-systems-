#!/usr/bin/python3.7
from predator_proie import *
import unittest



class TestpredatorProie(unittest.TestCase):

    def test_malthusien_model(self):
        """
        Test the malthusien model.
        """
        Y1=malthusiens(np.array([1000.]), 0., 2., 0.7, step_RK4, 2 )
        Y2=malthusiens(np.array([1000.]), 0., 2., 0.7, step_RK4, -2 ) 
        Y3=malthusiens(np.array([1000.]), 0., 2., 0.7, step_RK4, 0 ) 


        plt.plot(subdivision(0., 2., len(Y1)),Y1,"green",\
                 label="AUGMENTATION")
        plt.plot(subdivision(0., 2., len(Y2)),Y2, "blue",\
                 label="DIMINUTION")
        plt.plot(subdivision(0., 2., len(Y3)),Y3, "black",\
                 label="Population constante")


        plt.xlabel("temps")
        plt.ylabel("nombre d'individus")
        plt.axis([int(0),int(2),0,10000])
        plt.title("Evolution de la population selon le modele de Malthusiens")
        plt.legend()
        plt.show()


    def test_verhulst_model(self):
        """
        Test the verhulst model.
        """
        Y4=verhulst(np.array([1000.]), 0., 5., 0.7,  step_RK4, 2, 10000 )
        Y5=verhulst(np.array([1000.]), 0., 5., 0.7,  step_RK4, 2, 1000 ) 
        Y6=verhulst(np.array([1000.]), 0., 5., 0.7,  step_RK4, 2, 100 ) 


        plt.plot(subdivision(0., 2., len(Y4)),Y4,"green",\
                 label="limite a 10000")
        plt.plot(subdivision(0., 2., len(Y5)),Y5, "blue",\
                 label="limite a 1000")
        plt.plot(subdivision(0., 2., len(Y6)),Y6, "black",\
                 label="limite a 100")


        plt.xlabel("temps")
        plt.ylabel("nombre d'individus")
        plt.axis([int(0),int(2),0,10000])
        plt.title("Evolution de la population selon le modele de Verhulst")
        plt.legend()
        plt.show()

    def test_Lokta_Volterra_curves(self):
        """
        Test the Lokta Volterra model.
        """
        t0 = 0.
        tf = 365.
        eps = 0.8
        
        
        a = 0.25  
        b = 0.05  
        c = 0.01  
        d = 0.1   
        
    
        init = np.array([80., 20.]) 
        
        Y = Lotka_Volterra(a, b, c, d, init, t0, tf, eps)
        
        l = len(Y)
        Nt=np.zeros(l)
        Pt=np.zeros(l)
        for i in range(l):
            Nt[i] = Y[i][0]
            Pt[i] = Y[i][1]
   

        plt.plot(subdivision(t0, tf, l), Nt,"green",\
                 label="N(t), nombre des proies")
        plt.plot(subdivision(t0, tf, l), Pt,"purple",\
                 label="P(t), nombre des predateurs")
        plt.legend()
        plt.xlabel("temps")
        plt.ylabel("Population")
        plt.title("modele Lotka-Volterra")
        plt.axis([t0,tf,0,140])
        plt.show()
        
        
        plt.plot(Nt, Pt,"purple")
        plt.xlabel("Nombre de proies N(t)")
        plt.ylabel("Nombre de predateurs P(t)")
        plt.title(" P(t) en fonction de N(t),\n \
        avec le modele de Lotka-Volterra." )
        plt.show()
        
        print("Periode ",\
              round(periode(Nt, t0, tf),2))

    def test_diagramm_1(self):
        """
        Tests around (0, 0) point
        """
        t0 = 0.
        tf = 365.
        eps = 0.8
    
        a = 0.25  
        b = 0.05  
        c = 0.01  
        d = 0.1   
       
    
        for p in range(10):
        
            init = np.array([0.0 + p/10., 0.0 + p/10.])
            Y = Lotka_Volterra(a, b, c, d, init, t0, tf, eps)
            
            l = len(Y)
            Nt=np.zeros(l)
            Pt=np.zeros(l)
            for i in range(l):
                Nt[i] = Y[i][0]
                Pt[i] = Y[i][1]
            
            plt.plot(Nt, Pt,"purple")
        plt.xlabel("Nombre de proies N(t)")
        plt.ylabel("Nombre de predateurs P(t)")
        plt.title(" Resultats autour du point (0, 0)" )
        plt.show()

    def test_diagramm_2(self):
        """
        Tests around (d/c, a/b) point
        """
        t0 = 0.
        tf = 365.
        eps = 0.8
        
        a = 0.25  
        b = 0.05  
        c = 0.01  
        d = 0.1   
        
        #init = np.array([60., 10.]) #([proies,predateurs])
        for p in range(10):
        
            init = np.array([d/c + p/10., a/b + p/10.])
            Y = Lotka_Volterra(a, b, c, d, init, t0, tf, eps)
            
            l = len(Y)
            Nt=np.zeros(l)
            Pt=np.zeros(l)
            for i in range(l):
                Nt[i] = Y[i][0]
                Pt[i] = Y[i][1]
            
            plt.plot(Nt, Pt,"purple")
        for p in range(10):
        
            init = np.array([d/c - p/10., a/b - p/10.])
            Y = Lotka_Volterra(a, b, c, d, init, t0, tf, eps)
        
            l = len(Y)
            Nt=np.zeros(l)
            Pt=np.zeros(l)
            for i in range(l):
                Nt[i] = Y[i][0]
                Pt[i] = Y[i][1]
            
            plt.plot(Nt, Pt,"purple")
        plt.xlabel("Nombre de proies N(t)")
        plt.ylabel("Nombre de predateurs P(t)")
        plt.title(" Resultats autour du point (d/c, a/b)" )
        plt.show()
    
    
if __name__ == '__main__':
    unittest.main()
