import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import animation as animation

#def of random choice for i

def random(l):
    ''' enter the lenght of lattice '''
    ''' this function is a 2D random walker with deposition it  in a lattice'''
    ''' and also animate it.'''
    L = len(l)
    fig = plt. figure()
    img = []
    p =0.5
    p1 = [p,1-p]
    n = 0
    nn = 0
    h = np.zeros(200)
    while n<6000:
        
        hm = max(h) +20
        x = [n%100+1]
        y = [hm]
        j =0
        i = n%100+1
        while True:
            if x[j] < 200 and x[j] > 1 and y[j] < 10+hm and j<600:
                a = np.random.choice([1,-1] , p = p1)
                x.append (x[j]+a)
                b = np.random.choice([1,-1] , p = p1)
                y.append (y[j]+b)
                i = x[j+1]
                #print (i,j,y[j+1])
            else :
                break
            if i !=0 and i!= L-1 and y[j+1] <= max(h[i],h[i+1],h[i-1]):
                a = max(h[i], h[i+1],h[i-1])
                nn += 1

                if a == y[j+1]:
                    h[i] = h[i]+1
                else:
                    h[i] = a
                #print (h[i])
                break
            elif i == 0 and y[j+1] <= max(h[i], h[i+1],h[L-1]):
                a = max(h[i], h[i+1],h[L-1])

                nn += 1
                if a == y[j+1]:
                    h[i] = h[i]+1
                else:
                    h[i] = a
                break
            elif y[j+1] <= max(h[i], h[0],h[i-1]) :
                a = max(h[i], h[0],h[i-1])
                nn += 1

                if a == y[j+1]:
                    h[i] = h[i]+1
                else:
                    h[i] = a
                break

            j += 1
        print(nn)
        if nn <300 :
            img.append(plt.scatter(i,h[i],marker='s',s=0.5, color= 'b'))
            
        elif nn < 700 and nn>300:

            img.append(plt.scatter(i,h[i],marker='s',s=0.5, color= 'r'))
            

        elif nn < 1000  and nn>700:
            img.append(plt.scatter(i,h[i],marker='s',s=0.5, color= 'g'))
            

        elif nn < 7000 :
            img.append(plt.scatter(i,h[i],marker='s',s=0.5, color= 'r'))
            


    
        n +=1
    ani = animation.FuncAnimation(fig, img, interval=20, blit=True)
    ani.save('animation-marjan.gif',writer= 'pillow',fps=50)
    #fig.savefig('marjan.png')
    plt.show()
    return h
########################################   

l = list(range(200))
L = len(l)

#animation


Z   = []
Z = random (l )
np.savetxt("h.txt",Z)




