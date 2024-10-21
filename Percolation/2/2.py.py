import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.cm as cm
from statistics import mean
from statistics import variance
from statistics import stdev


for p in [0.5]: 
        p1 = [p,1-p]
        x = [0]
        var = []
        X =[]

        for i in range (30000):
            a = np.random.choice([1,-1] , p = p1)
            x.append (x[i]+a)
            X.append(mean(x))
            var.append(variance(x))
            print (i)
        np.savetxt("x30"+str(p)+".txt",x)
        np.savetxt("xmean30"+str(p)+".txt",X)
        np.savetxt("xvar30"+str(p)+".txt",var)
        
        
 #plot
fig = plt .figure()
N =np.arange(30000)
xmean = []
var = []

for p in [0.5]:
    x = xmean = np.loadtxt("x30"+str(p)+".txt")
    xmean = np.loadtxt("xmean30"+str(p)+".txt")
    var = np.loadtxt("xvar30"+str(p)+".txt")
    plt.plot(N,x[1:] ,'.')
    plt.xlabel(" N")
    plt.ylabel("x")
    plt.legend(['p ='+str(p)],loc = 'upper left')
    #fig.savefig('p1'+str(p)+'15.png')
    plt.show()
    
    m= np.polyfit(N, xmean,1)
    M = np.polyfit(N,var,1)
    
    plt.plot(N,xmean ,'.', N , N*m[0]+m[1])
    plt.plot(N,var ,'.', N , N*M[0]+M[1])
    
    plt.xlabel(" N")
    plt.ylabel("x")
    plt.legend(['xmean p-'+str(p),'m_xmean p-'+str(p)+'='+str(m[0]),'variance_X p-'+str(p),'variance_X  p-'+str(p)+'='+str(M[0])],loc = 'upper left')
    #fig.savefig('p2'+str(p)+'15.png')
    plt.show()
