import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from matplotlib import animation as animation
from statistics import mean
from statistics import stdev


#def of random choice for i

def random_t(l,h):
	L = len(l)

	i = int(np.random.choice(l))
	if i !=0 and i!= L-1:
		a = min(h[i], h[i+1],h[i-1])
		if a == h[i] and a == h[i+1]:
			m =  int(np.random.choice([i ,i+1]))
			h[m] = h[m] + 1
		elif a == h[i] and a == h[i-1]:
			m =  int(np.random.choice([i ,i-1]))
			h[m] = h[m] + 1	
		elif a == h[i-1] and a == h[i+1]:
			m =  int(np.random.choice([i-1 ,i+1]))
			h[m] = h[m] + 1							
		elif a == h[i+1]:
			h[i+1] = h[i+1]+1
		elif a == h[i-1]:
			h[i-1] = h[i-1]+1
		elif a == h[i]:
			h[i] = h[i]+1

	elif i == 0:
		a = min(h[i], h[i+1],h[L-1])
		if a == h[i] and a == h[i+1]:
			m =  int(np.random.choice([i ,i+1]))
			h[m] = h[m] + 1
		elif a == h[i] and a == h[L-1]:
			m =  int(np.random.choice([i ,L-1]))
			h[m] = h[m] + 1	
		elif a == h[L-1] and a == h[i+1]:
			m =  int(np.random.choice([L-1 ,i+1]))
			h[m] = h[m] + 1							
		elif a == h[i+1]:
			h[i+1] = h[i+1]+1
		elif a == h[L-1]:
			h[L-1] = h[L-1]+1
		elif a == h[i]:
			h[i] = h[i]+1

	else :
		a = min(h[i], h[i-1],h[0])
		if a == h[i] and a == h[0]:
			m =  int(np.random.choice([i ,0]))
			h[m] = h[m] + 1
		elif a == h[i] and a == h[i-1]:
			m =  int(np.random.choice([i ,i-1]))
			h[m] = h[m] + 1	
		elif a == h[i-1] and a == h[0]:
			m =  int(np.random.choice([i-1 ,0]))
			h[m] = h[m] + 1							
		elif a == h[0]:
			h[0] = h[0]+1
		elif a == h[i-1]:
			h[i-1] = h[i-1]+1
		elif a == h[i]:
			h[i] = h[i]+1
		
			
							
	return h
	
	
# def of plot uniform of deposition
def plot(n_max,l):
	L = len(l)
	h = np.zeros(L)
	h1 = np.zeros(L)
	n=0
	while n < n_max:

# random choice
		i = int(np.random.choice(l))
		if i !=0 and i!= L-1:
			a = min(h[i], h[i+1],h[i-1])
			if a == h[i] and a == h[i+1]:
				m =  int(np.random.choice([i ,i+1]))
				h[m] = h[m] + 1
			elif a == h[i] and a == h[i-1]:
				m =  int(np.random.choice([i ,i-1]))
				h[m] = h[m] + 1	
			elif a == h[i-1] and a == h[i+1]:
				m =  int(np.random.choice([i-1 ,i+1]))
				h[m] = h[m] + 1							
			elif a == h[i+1]:
				h[i+1] = h[i+1]+1
			elif a == h[i-1]:
				h[i-1] = h[i-1]+1
			if a == h[i]:
				h[i] = h[i]+1
		elif i == 0:
			a = min(h[i], h[i+1],h[L-1])
			if a == h[i] and a == h[i+1]:
				m =  int(np.random.choice([i ,i+1]))
				h[m] = h[m] + 1
			elif a == h[i] and a == h[L-1]:
				m =  int(np.random.choice([i ,L-1]))
				h[m] = h[m] + 1	
			elif a == h[L-1] and a == h[i+1]:
				m =  int(np.random.choice([L-1 ,i+1]))
				h[m] = h[m] + 1							
			elif a == h[i+1]:
				h[i+1] = h[i+1]+1
			elif a == h[L-1]:
				h[L-1] = h[L-1]+1
			if a == h[i]:
				h[i] = h[i]+1

		else :
			a = min(h[i], h[i-1],h[0])
			if a == h[i] and a == h[0]:
				m =  int(np.random.choice([i ,0]))
				h[m] = h[m] + 1
			elif a == h[i] and a == h[i-1]:
				m =  int(np.random.choice([i ,i-1]))
				h[m] = h[m] + 1	
			elif a == h[i-1] and a == h[0]:
				m =  int(np.random.choice([i-1 ,0]))
				h[m] = h[m] + 1							
			elif a == h[0]:
				h[0] = h[0]+1
			elif a == h[i-1]:
				h[i-1] = h[i-1]+1
			if a == h[i]:
				h[i] = h[i]+1	
		if n == 30000:
			for j in range (L):
				
				plt.bar(j,h[j]-h1[j],bottom=h1[j],width=1, color= 'b')
				h1[j] = h[j] 
		if n == 67000:
			for j in range (L):
				
				plt.bar(j,h[j]-h1[j],bottom=h1[j],width=1, color= 'r')
				h1[j] = h[j] 
		if n == 99000:
			for j in range (L):
				
				plt.bar(j,h[j]-h1[j],bottom=h1[j],width=1, color= 'b')
				h1[j] = h[j] 
		n += 1
	plt.show()
	
		
	
#basic information
l = list(range(150))
L = len(l)
n_max=10**5
#a = np.zeros(100)
b = np.zeros((10,100))
B =  np.zeros((10,100))
T= []


## plot variace and avrage height


"""m=0
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
plt.show()"""
for q in range(10):
	c= np.zeros(L)
	m=0
	for i in range(4400000):
		c = random_t(l,c)
		if i % int((1.2)**m) == 0 :
			#a [m] = mean(c)
			b [q][m] = stdev(c)
			print(b[q][m])
			T.append (i)
			m += 1
np.savetxt ( "w-t seurface relaxation-10-150.txt",b )
np.savetxt ( "t10-150.txt",T )


