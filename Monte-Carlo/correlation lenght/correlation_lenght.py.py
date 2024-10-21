import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from matplotlib import animation as animation

#def of random choice for i
n=0
def random_t(t,l):
	L = len(l)
	h = np.zeros(L)
	h[100] = 1
	q = 0
	c = []
	while h[0]<=250 and h[L]<=250:

		i = int(np.random.choice(l))
		if i !=0 and i!= L-1 :
			a = max(h[i], h[i+1],h[i-1])
			if i==100 or a!=0:

				if a == h[i]:
					h[i] = h[i]+1
				else:
					h[i] = a
		elif i == 0:
			a = max(h[i], h[i+1],h[L-1])
			if i==100 or a!=0:

				if a == h[i]:
					h[i] = h[i]+1
				else:
					h[i] = a
		else :
			a = max(h[i], h[0],h[i-1])
			if i==100 or a!=0:

				if a == h[i]:
					h[i] = h[i]+1
				else:
					h[i] = a
		n +=1
							
	return h
	
# def of plot uniform of deposition
def plot(n_max,l):
	L = len(l)
	h = np.zeros(L)
	h1 = np.zeros(L)
	n=0
	h[100] = 1
	T =[]
	cor =[]
	while h[0]<=250 and h[L-1]<=250:


		i = int(np.random.choice(l))
		if i !=0 and i!= L-1 :
			a = max(h[i], h[i+1],h[i-1])
			if i==100 or a!=0:

				if a == h[i]:
					h[i] = h[i]+1
				else:
					h[i] = a
		elif i == 0:
			a = max(h[i], h[i+1],h[L-1])
			if i==100 or a!=0:

				if a == h[i]:
					h[i] = h[i]+1
				else:
					h[i] = a
		else :
			a = max(h[i], h[0],h[i-1])
			if i==100 or a!=0:

				if a == h[i]:
					h[i] = h[i]+1
				else:
					h[i] = a		
				
		if n%1000 ==0 :
			cor.append( np.count_nonzero( h))
			T.append(n)
			i += 1
			#c.append(cor) 		
		if n <3000:
			plt.scatter(i,h[i],marker='.',s=1, color= 'b') 
		if n < 6000 and n>3000:
			plt.scatter(i,h[i],marker='.',s=1, color= 'r')
		if n < 8000 and n>6000:
			plt.scatter(i,h[i],marker='.',s=1, color= 'b')

		if n < 10000:
			plt.scatter(i,h[i],marker='.',s=1, color= 'r')
		n += 1
	np.savetxt("correlation2.txt",cor)
	np.savetxt("number cor.txt",T)
	plt.show()

	
	
#basic information
l = list(range(200))
L = len(l)
n_max=100000
c = np.zeros((22,2))
c1 = np.zeros(21)
c2 = np.zeros(21)

plot(n_max,l)

