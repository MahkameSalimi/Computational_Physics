import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from matplotlib import animation as animation

# Image width and height; parameters for the plot


a=0
def julia(i,a):
	
	# define c
	a = a + i* (np.pi/180)
	c =np.exp(complex(0, a))
	
	n_max = 700 # tedad tekrar tabe bar har noghte faza ke dakhe dayere be shoa 8 hastand
	nx, ny = 300, 300
	julia = np.zeros((nx, ny))
	for ix in range(nx):
		for iy in range(ny):
			N = 0
			# Map pixel position to a point in the complex plane
			z = complex(ix*(3/nx) -1.5  ,
				    iy*(3/ny)-1.5)
			# Do the iterations
			while abs(z) <= 8 and N < n_max:
			    z = z**2 + c
			    N += 1
			julia[ix][iy] = N%100
	return julia


fig, ax = plt.subplots()

ax.imshow(julia(190,0), cmap=cm.twilight)
# animation
"""fig = plt.figure()
plt.axis('off')
Z   = []
img = []
for i in range(360):
	
	Z.append(julia(i,0))
	img.append([plt.imshow(Z[i],cmap=cm.twilight)])
    	
ani = animation.ArtistAnimation(fig, img, interval=20, blit=True)
#ani = animation.FuncAnimation(fig, animate, interval=400, blit=False)
ani.save('animation-julia.gif',writer= 'pillow',fps=30)"""

plt.show()
