import os
import numpy as np
import matplotlib.pyplot as plt

os.system("g++ pasos.cpp -o dat.x")
os.system("./dat.x > datos.dat")

data = np.loadtxt("datos.dat")

plt.figure()
plt.plot(data[:,0], data[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Caminata Aleatoria')
plt.savefig("datos.png")