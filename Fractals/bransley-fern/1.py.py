import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

f1 = lambda x,y: (0., 0.16*y)
f2 = lambda x,y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
f3 = lambda x,y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
f4 = lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
fs = [f1, f2, f3, f4]



img = np.zeros((500,500))

x, y = 0, 0
for i in range(50000):
    # Pick a random transformation and apply it
    f = np.random.choice(fs, p=[0.01, 0.85, 0.07, 0.07])
    x, y = f(x,y)
    print (x,y)
    ix, iy = int(250+ x * 50), int(y *  50)
    # Set this point of the array to 1 to mark a point in the fern
    img[iy, ix] = 1

plt.imshow(img[::-1,:], cmap=cm.Greens)
plt.show()
