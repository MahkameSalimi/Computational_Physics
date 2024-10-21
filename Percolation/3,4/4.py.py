import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.cm as cm
from statistics import mean
from statistics import variance
from statistics import stdev

for p in [0.3,0.5,0.8]:
    n1 = []
    for m in range (20):
        n =[]
        a = np.zeros((100,20))
        a[0][m] = 1
        for i in range (99):

            for j in range (20):

                if a[i][j] != 0 and j != 0 and j != 19:
                    a[i+1][j+1] = a[i+1][j+1]+a[i][j]*p
                    a[i+1][j-1] = a[i+1][j-1] + a[i][j]*(1-p)

            if sum(a[i][:]) < 0.3:
                n.append(i)
                break
        n1 .append(n)
        np.savetxt("N"+str(p)+".txt",n1)


            
  #plot
N =[]
l = np.arange(20)
for p in [0.3,0.5,0.8]:
    N= np.loadtxt("N"+str(p)+".txt")
    plt . plot(l, N, '.-')
    plt.legend(['Tmean P-'+str(p)+' ,l_max='+str(np.argmax(N)),'run = 100000'],loc = 'upper left')
    plt.xlabel(" L")
    plt.ylabel("T")
    plt.show()
