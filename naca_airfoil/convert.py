import os
import subprocess
from subprocess import call

def convert(num_nodes):
        for filename in os.listdir('/home/emil/Project/naca_airfoil/msh'):
                if filename.endswith(str(num_nodes) + ".msh"):
                        name = "dolfin-convert " + "/home/emil/Project/naca_airfoil/msh/" + filename + " /home/emil/Project/naca_airfoil/msh/" + filename + ".xml"
                        subprocess.call(name, shell=True)

convert(150)
