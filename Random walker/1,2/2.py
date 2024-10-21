import matplotlib.pyplot as plt
import numpy as np


#for n in range(80000,100000,1000):
for n in [100000]:
    h = np.zeros(10)
    for i in range (n):
        #choose a number between 0 , 10
        x = np.random.randint (0,10)
        y = np.random.randint (0,10)
        if y == 4 :
        
            h[x] = h[x] +1
    #plot the distribution 
    plt.bar(range(10),h)
    plt.plot(range(10),h,color = 'r')
    plt.legend(['n='+str(n)])
    plt.xlabel(" N")
    plt.ylabel("H")
    
    plt.show()
