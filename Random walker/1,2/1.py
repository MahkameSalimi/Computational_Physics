import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from statistics import variance
from statistics import stdev

sigma =[]
for n in range(1000,30000,1000):
    h = np.zeros(10)
    for i in range (n):
        #choose a number between 0 , 10
        x = np.random.randint (0,10)
        h[x] = h[x] +1
    #plot the distribution 
    plt.bar(range(10),h)
    plt.plot(range(10),h, color ='g')
    plt.legend(['n='+str(n)])
    plt.xlabel(" N")
    plt.ylabel("H")
    sigma.append(stdev(h)/n)
    plt.show()
    #plot sigma/n , N and fine the slope
N = range(1000,30000,1000)
m = np.polyfit(np.log(N),np.log(sigma),deg=1)
plt.plot(np.log(N),np.log(sigma),np.log(N),m[0]*np.log(N)+m[1])
plt.legend(['sigma/n','m = '+str(m[0])])
plt.xlabel(" log(N)")
plt.ylabel("log(sigma/n)")

plt.show()
