import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.cm as cm
from statistics import mean


for p in [0.3,0.5,0.8]:
    n1 =[]
    n2 = []
    for j in range (20):
        
        p1 = [p,1-p]
        
        N =[]
        n =0 
        while n!= 15000:
            x = [j]
            for i in range (1000):
                a = np.random.choice([1,-1] , p = p1)
                x.append (x[i]+a)
                #print (x)
                if x[i]+a == 20 or x[i]+a == 0:
                    N.append(i)
                    break
            n += 1
        n1.append(mean(N))
    print (p)
    np.savetxt("N"+str(p)+".txt",n1)
    
    
    #plot
N =[]
var = []
l = np.arange(20)
for p in [0.3,0.5,0.8]:
    N= np.loadtxt("N"+str(p)+".txt")
    #var = np.loadtxt("cor2"+str(p)+".txt")
    plt . plot(l[1:], N[1:], '.-')
    #plt . plot(l, var , '.-')
    plt.legend(['Tmean P-'+str(p),'varianceT p-'+str(p),'run = 100000'],loc = 'upper left')
    plt.xlabel(" L")
    plt.ylabel("T")
    plt.show()
