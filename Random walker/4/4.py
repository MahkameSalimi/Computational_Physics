import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev

sigma = 1.2
y1 =[]
y2 =[]
for j in range (100000):

        #choose a number between 0 , 1

    x0 = np.random.uniform (0,1)
    x1 = np.random.uniform (0,1)

    y1.append(np.sqrt(-2*sigma**2*np.log(x1))*np.sin(2*np.pi*x0))
    y2.append(np.sqrt(-2*sigma**2*np.log(x1))*np.sin(2*np.pi*x0))
                     
                
    #plot the distribution 
y =np.concatenate((y1,y2))
plt.hist(y,color ='r',bins=100)
plt.legend(['y1,y2 , sigma = '+str(stdev(y))])
plt.xlabel(" N")
plt.ylabel("H")
plt.show()
