import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev

from statistics import mean
sigma= []

for n in [5,10,100,1000]:
#for n in [5]:
    H =[]
    for j in range (100000):
        h =[]
        for i in range (n):
        #choose a number between 0 , n

            x = np.random.randint (0,9)
            h.append(x)
                     
                     
            
        H.append(mean(h))
                
    #plot the distribution 
    sigma.append(stdev(H))
    plt.hist(H,bins=70)
    plt.legend(['n ='+str(n)+' sigma = '+str(stdev(H))])
    plt.xlabel(" N")
    plt.ylabel("H")
    plt.show()
