import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from matplotlib import animation as animation
from statistics import mean
from statistics import variance
from statistics import stdev
#def of random choice for i

def random(l,h):
	L = len(l)

	i = int(np.random.choice(l))
	if i !=0 and i!= L-1:
		a = max(h[i], h[i+1],h[i-1])

		if a == h[i]:
			h[i] = h[i]+1
		else:
			h[i] = a
	elif i == 0:
		a = max(h[i], h[i+1],h[L-1])

		if a == h[i]:
			h[i] = h[i]+1
		else:
			h[i] = a
	else :
		a = max(h[i], h[0],h[i-1])

		if a == h[i]:
			h[i] = h[i]+1
		else:
			h[i] = a		
									
	return h
	
# def of plot uniform of deposition
def plot(n_max,l):
	L = len(l)
	h = np.zeros(L)
	h1 = np.zeros(L)
	n=0
	while n < n_max:


		i = int(np.random.choice(l))
		if i !=0 and i!= L-1:
			a = max(h[i], h[i+1],h[i-1])

			if a == h[i]:
				h[i] = h[i]+1
			else:
				h[i] = a
		elif i == 0:
			a = max(h[i], h[i+1],h[L-1])

			if a == h[i]:
				h[i] = h[i]+1
			else:
				h[i] = a
		else :
			a = max(h[i], h[0],h[i-1])

			if a == h[i]:
				h[i] = h[i]+1
			else:
				h[i] = a		
				
			
				
		if n <3000:
			plt.scatter(i,h[i],marker='s',s=0.7, color= 'b') 
		if n < 6700 and n>3000:


			plt.scatter(i,h[i],marker='s',s=0.7, color= 'r') 

		if n < 10000:
			plt.scatter(i,h[i],marker='s',s=0.7, color= 'b') 
		n += 1
	plt.show()
	
	
#basic information
l = list(range(90))
L = len(l)
n_max=10000
#plot(n_max,l)



## plot variace and avrage height
b = np.zeros((10,100))
"""
m=0
for t in T:
	c = random_t( t, l)
	a [m] = mean(c)
	m += 1
n1 , b1 = np.polyfit(T,a,1)
M1 = float(n1)
B1 = float(b1)
im1 = plt.plot( T,a,'.',T, M1*(T)+B1,'--k',label="n = 10^5")
plt.xlabel(" t")
plt.ylabel(" average_height (t)")
plt.show()

"""
T =[]
for q in range(10):
	c= np.zeros(L)
	m=0
	for i in range(600000):
		c = random(l,c)
		
		if i %int((1.2)**m) == 0 :
		# variance
			b [q][m] = stdev(c)
			print( b[q][m])
			T.append (i)
			m += 1
np.savetxt ( "w-tdeposithion-10-70.txt",b )
np.savetxt ( "t-d-10-70.txt",T )


