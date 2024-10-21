import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
N =100 
L = 20
v = np.arange (-3,3,0.01)
data = np.zeros((N,4))
c =0 
d= 0
for i in range(N+1):
    if i % (N/(L/2)) == 0 and i != 0:
        data [d:i,0] = np.arange(L/2) 
        data [d:i,1] = c 
        c +=1
        d = i
for i in range(N):
    data [i,0] = np.random.choice(range(5))
    data [i,1] = np.random.choice(range(5))
    data [i,2] = np.random.choice(v)
    data [i,3] = np.random.choice(v)
data [:,2] = data[:,2]-np.mean(data[:,2])
data [:,3] = data[:,3]-np.mean(data[:,3])


def timestep1 ():

    data[:,:2] += data[:, 2:]
    #periodic boundrey
    cross_left = data [:,0]<0
    cross_right = data [:,0]>L
    cross_top = data [:,1]>L
    cross_bot = data [:,1]<0
    
    
    data[cross_left , 0] += L
    data[cross_right , 0] -= L
    data[cross_top, 1] -= L
    data[cross_bot, 1] += L
    
    return
####################


def r2 (N, L):
    
    
    rc =2.5
    r2 = np.zeros((N,N))
    for i in range(N):
        for j in range (i , N):
            x = (data[j,0]-data[i,0])
            y =  (data[j,1]-data[i,1])
            if abs (x) < L/2 and abs (y) < L/2 :

                if x < 2 *rc and y < 2*rc:

                    r2[i][j] = x*x + y*y
            if abs (x) > L/2 and abs (y) < L/2 :

                if min (abs (x+L) , abs(x-L)) < 2 *rc and y < 2*rc:

                    r2[i][j] = min (abs (x+L) , abs(x-L))**2 + y*y
            if abs (x) < L/2 and abs (y) >L/2 :

                if min (abs(y+L) , abs(y-L)) < 2 *rc and x < 2*rc:

                    r2[i][j] = min (abs(y+L) , abs(y-L))**2 + x*x
            if abs (x) > L/2 and abs (y) > L/2 :

                if min (abs (x+L) , abs(x-L)) < 2 *rc and min (abs(y+L) , abs(y-L)) < 2*rc:

                    r2[i][j] = min (abs (x+L) , abs(x-L))**2+ min (abs(y+L) , abs(y-L))**2
    
    for i in range(N):
        for j in range (i , N):
            r2[j][i] = r2 [i][j]
            
    return r2
    
 

import matplotlib
xs = data[: , 0]
vx = data [:,2]
ys = data[:, 1]
vy = data [:,3]
fig, ax = plt.subplots()
line, = ax.plot ([],[],'b.',ms= 16)

ax.set_xlim(0,L)
ax.set_ylim(0,L)
def kinetic():
    return 0.5*np.sum(data[:,2:]*data[:,2:])
def collision():

    timestep1 ()
    R2 = np .zeros((N,N))
    R2 = r2 (N, L)
    u = []
    ax = []
    ay = []
    k =[]
    frx =[]
    fry =[]
    for i in range (N):
        for j in range (N):
            r_2 = R2[i][j]
            r4 = r_2 * r_2
            r6= r4 * r_2
            r12 = r6 *r6
            x = (data[j,0]-data[i,0])
            y =  (data[j,1]-data[i,1])
            u.append(np.sum(4*(1/(r12)-1/(r6))))
            ax .append( np.sum(24*(2/r12-1/r6)*(x/r_2)))
            ay.append(np.sum(24*(2/r12-1/r6)*y/r_2))
    for i in range (N):
        for j in range (N):
            x = (data[j,0]-data[i,0])
            y =  (data[j,1]-data[i,1])
            frx.append(ax[i] . x)
            fry.append(ay[i] . y)
            

    return [ax,ay,frx,fry,np.sum(u)]
                
def timestep(q):
    dt = 0.001
    timestep1()
    FRX = collision()[2]
    FRy= collision()[3]
    
    ax = collision()[0]

    ay = collision()[1]

    for i in range(N):
        data[i,0] = data[i,0] + data[i,2]*dt+0.5*ax[i]*dt*dt
        data[i,2] = data[i,2] + 0.5*ax[i]*dt
        data[i,1] = data[i,1] + data[i,3]*dt+0.5*ay[i]*dt*dt
        data[i,3] = data[i,3] + 0.5*ay[i]*dt
    ax = collision()[0]
    ay = collision()[1]
    for i in range(N):
        data[i,2] = data[i,2] + 0.5*ax[i]*dt
        data[i,3] = data[i,3] + 0.5*ay[i]*dt
    #k.append(kinetic())


q =0
# def ani (i):
#     timestep (q)
#     line.set_data(xs ,ys)
#     return line,

# ani = matplotlib.animation.FuncAnimation(fig, ani, interval =10)
#plt.show()





def particles_in_left():
    l=0
    for i in range(N):
        if dots[i,0]<=L/2:
            l=l+1
    return(l)

number= []
ps=[]
for t in range (10000):
    dt = 0.001
    timestep1()
    ax = collision()[0]

    ay = collision()[1]

    for i in range(N):
        data[i,0] = data[i,0] + data[i,2]*dt+0.5*ax[i]*dt*dt
        data[i,2] = data[i,2] + 0.5*ax[i]*dt
        data[i,1] = data[i,1] + data[i,3]*dt+0.5*ay[i]*dt*dt
        data[i,3] = data[i,3] + 0.5*ay[i]*dt
    ax = collision()[0]
    ay = collision()[1]
    for i in range(N):
        data[i,2] = data[i,2] + 0.5*ax[i]*dt
        data[i,3] = data[i,3] + 0.5*ay[i]*dt
for i inrange (10000):    
    k.append(kinetic())
    number.append(particles_in_left())
    ps.append((N/L**2)*(k[i]-0.5*(FRX[i]+FRY[i]))
    
#energy 
e =[]
U = []
t = range (10000)
for i in range (10000):
        U .append (collision()[4])
        e.append(U+k[i])

plt.plot(t,U,label="potential_energy")
plt.plot(t,k,label="kinetic_energy")
plt.plot(t,e,label="total_energy")
plt.legend(["potential_energy","kinetic_energy","total_energy"])
plt.show()

#number
plt.xlabel("time in unite of step") 
plt.ylabel('number of particle in left hand side of box')
plt.plot(ts,number)
plt.show()

#tempeture

for i in range (10000):
    T.append(k[i]/N-1)
    eror.append((np.var(T))**0.5)
fig, ax = plt.subplots()
ax.errorbar(t,T,yerr=eror)    
plt.plot(t,T)#,ts,fit1)
plt.xlabel("t") 
plt.ylabel('tempresure')
plt.show()

#presure

pf.append(np.mean(ps))
eror.append((np.var(ps))**0.5)
fig, ax = plt.subplots()
ax.errorbar(t,pf,yerr=eror)              
plt.plot(t,pf)
plt.xlabel("t") 
plt.ylabel('pressure')
plt.show()
              

