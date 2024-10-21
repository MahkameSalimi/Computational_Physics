from statistics import mean
from statistics import variance
from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.cm as cm

l=100
s=[]
r = np.zeros(200)


for y in range (200):
    c = np.zeros((l+2,l+2))
    # 9 is off
    # 0 is ground cell
    # 1 is on
    for i in range (l+2):
        for j in range(l+2):
            if i==0 or i==l+1:
                c[i][j] = 9
            if j==0 or j==l+1:
                c[i][j] = 9
    i1 = int(l/2)
    j1 = int(l/2)
    a = []
    b=[]
    a.append(i1)
    b.append(j1)

    c[int(l/2)][int(l/2)] = 1
    p1=[0.5,0.5]
    m = 0
    while True:
        i = a[m]
        j = b[m]

        if c[i+1][j] == 0 :    
            c[i+1][j] =  np.random.choice ([1,9], p = p1)
            if c[i+1][j] != 9 : 
                a.append(i+1)
                b.append(j) 
        if c[i-1][j] == 0 : 
            c[i-1][j] =  np.random.choice ([1,9], p = p1)
            if c[i-1][j] != 9 : 
                a.append(i-1)
                b.append(j) 
        if c[i][j+1] == 0 : 
            c[i][j+1] =  np.random.choice ([1,9], p = p1)
            if c[i][j+1] != 9 : 
                a.append(i)
                b.append(j+1) 
        if c[i][j-1] == 0 : 
            c[i][j-1] =  np.random.choice ([1,9], p = p1)
            if c[i][j-1] != 9 : 
                a.append(i)
                b.append(j-1)

        m +=1
        if m == len(a):
            break
    r[y]= np.sqrt(np.std(a)**2 +np.std(b)**2)
    s.append(m)
np.savetxt ( "R3.txt",r)
np.savetxt ( "s3.txt",s )
p = np .mean (r)
p2= np.mean (s)
B1 = np.log(np.loadtxt ( "R3.txt" ))
B2 = np.log(np.loadtxt ( "s3.txt" ))

#n3 , b3 = np.polyfit(B1,B2,1)
#M3 = float(n3)
#B3 = float(b3)
#print(M3)
im2 = plt.plot(B1,B2,'.')


plt.xlabel(" log S")
plt.ylabel(" Log R")
plt.show()
