import os
import subprocess
from subprocess import call

def airfoil(num_nodes):
        #airfoil arguments
        num_samples = '10'
        viscosity = '0.0001'
        speed = '10.0'
        time = '1'

        for filename in os.listdir('/home/emil/Project/naca_airfoil/msh'):
                if filename.endswith(str(num_nodes) + ".msh.xml"):
                        name = './navier_stokes_solver/airfoil ' + num_samples + ' ' + viscosity + ' ' + speed + ' ' + time + ' msh/' + filename
                        print name
                        #subprocess.call(name, shell=True)

airfoil(150)
