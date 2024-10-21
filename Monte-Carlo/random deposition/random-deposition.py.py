import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from matplotlib import animation as animation
from statistics import mean
from statistics import variance
from statistics import stdev
#def of random choice for i

def random_t(t,l):
	L = len(l)
	h = np.zeros(L)
	for n in range (t):

		i = int(np.random.choice(l))
		h[i] = h[i]+1

	return h
					 
# def of plot uniform of deposition
def plot(n_max,l):
	L = len(l)
	h = np.zeros(L)
	h1 = np.zeros(L)
	n=0
	while n < n_max:
		i = int(np.random.choice(l))
		h[i] = h[i]+1
		
		if n == 30000:
			for i in range (200):
				
				plt.bar(i,h[i]-h1[i],bottom=h1[i],width=1, color= 'b')
				h1[i] = h[i] 
		if n == 67000:
			for i in range (200):

				plt.bar(i,h[i]-h1[i],bottom=h1[i],width=1, color= 'r')
				h1[i] = h[i]
		if n == 99000:
			for i in range (200):

				plt.bar(i,h[i]-h1[i],bottom=h1[i],width=1, color= 'b')
				h1[i] = h[i]
		n += 1
	plt.show()
	

#basic information
l = np.array(range(200))
L = len(l)
n_max=10**5
T = np.array([100,400,1600,3200,6400,12800,25600,51200,102400,20000,40000,60000,70000,80000,90000,100000])
#T = list(range(100))

a = np.zeros(len(T))
b = np.zeros(len(T))

# plot variace and avrage height
m=0
"""for t in T:
	c = random_t( t, l)
	a [m] = mean(c)
	m += 1

n1 , b1 = np.polyfit(T,a,1)
M1 = float(n1)
B1 = float(b1)
im1 = plt.plot( T,a,'s',T, M1*(T)+B1,'--k',label="n = 10^5")
plt.xlabel(" t")
plt.ylabel(" average_height (t)")
	

plt.show()"""

for t in T:
	c = random_t( t, l)
	a [m] = mean(c)
	b [m] =	stdev (c, a[m])
	m += 1
	
n2 , b2 = np.polyfit(np.log(T),np.log(b),1)
M2 = float(n2)
B2 = float(b2)

im2 = plt.plot( np.log(T),np.log(b),'s',np.log(T), M2*(np.log(T))+B2,'--k',label="n = 10^5")

#im = plt.plot( T,b,'s')
plt.xlabel(" t")
plt.ylabel(" variance (t)")

plt.show()
"""
# calculate average of beta
B = np.zeros(10)
for i in range (10):
	m=0
	for t in T:
		c = random_t( t, l)
		a [m] = mean(c)
		b [m] = stdev(c,a[m])
		m += 1
		
	beta ,p = np.polyfit(np.log(T),np.log(b),1)

	B[i] = float(beta)
	
BETA = mean (B)
print ( " average value of beta is", BETA)
#plot(n_max,l)"""




