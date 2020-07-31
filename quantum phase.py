# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:23:08 2018

@author: a.borrallo.rentero
"""

if __name__ == '__main__':

    import Qconfig
    import qiskit
    import numpy as np
    from qiskit import QuantumProgram 
    import math
    from qiskit.tools.visualization import plot_histogram
    from qiskit import Gate
    from qiskit import CompositeGate
    from scipy.optimize import newton
    from sympy import *
    from sympy.physics.quantum.circuitplot import CircuitPlot,labeller,Mz,CreateOneQubitGate
    from sympy.physics.quantum.gate import *
    from sympy.physics.quantum.qasm import Qasm,CGate,Z
    import operator
    from functools import reduce
    
    U=np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1/math.sqrt(2),1/math.sqrt(2)],[0,0,-1/math.sqrt(2),1/math.sqrt(2)]])
    CU=np.matrix([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1/math.sqrt(2),1/math.sqrt(2)],[0,0,0,0,0,0,-1/math.sqrt(2),1/math.sqrt(2)]])
    CU2=np.dot(CU,CU)
    CU3=np.dot(CU2,CU)
    CU4=np.dot(CU3,CU)
    U2=np.dot(U,U)
    U3=np.dot(U2,U)
    U4=np.dot(U3,U)
    print(CU4)
    print(U4)
    Operador1=(1/math.sqrt(2))*np.matrix([[0,0,math.sqrt(2),0],[0,0,0,math.sqrt(2)],[-1j,1,0,0],[1,-1j,0,0]])
    Operador2=(1/math.sqrt(2))*np.matrix([[0,0,math.sqrt(2),0],[0,0,0,math.sqrt(2)],[1j,1,0,0],[1,1j,0,0]])
   

 #check  
    #print(Operador1)
    #print(np.dot(np.matrix.transpose(np.matrix.conjugate(U)),U))
    #print(np.dot(np.matrix.transpose(np.matrix.conjugate(U2)),U2))
    #print(np.dot(np.matrix.transpose(np.matrix.conjugate(U3)),U3))
    #print(np.dot(np.matrix.transpose(np.matrix.conjugate(U4)),U4))
    #print(np.dot(np.matrix.transpose(np.matrix.conjugate(Operador1)),Operador1))
    #print(np.dot(np.matrix.transpose(np.matrix.conjugate(Operador2)),Operador2))
    
    