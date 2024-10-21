import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.cm as cm
from statistics import mean

for p in [0.5]:
    n1 =[]
    r2 = []
    p1 = [p,1-p]
    n =0 
    x = [0]
    y = [0]

    for i in range (30000):
        a = np.random.choice([1,-1] , p = p1)
        x.append (x[i]+a)
        b = np.random.choice([1,-1] , p = p1)
        y.append (y[i]+b)

        r2.append(mean(np.array(x)**2+np.array(y)**2))
        print(i)
    np.savetxt("r10"+str(p)+".txt",r2)
    
#plot


N =np.arange(30000)
fig = plt.figure()
p =0.5
r = np.loadtxt("r300.5.txt")
m=[]
m = np.polyfit(N,r,1)
print('m = ',m)
plt.plot(N ,r,'.',N, m[0]*N+m[1])
plt.legend(['N-p'+str(p)+' = 30000','m ='+str(m[0])],loc = "upper left")
fig.savefig('p'+str(p)+'50-2D.png')
