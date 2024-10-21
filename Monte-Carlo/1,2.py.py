import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.cm as cm

l = 20
k = np.zeros((l,l))

for i in range (l):
    for j in range (l):
        k[i][j] =  np.random.choice ([1,0], p = [0.6,0.4])
#plt.imshow(k,cmap=cm.gray)
#plt.show()
k2 = np.ones((l,1))
k1 = np.concatenate((k2,k,k2-1),axis = 1)
k2 = np.zeros((1,l+2))
k1 = np.concatenate((k2,k1),axis = 0)
d = 1
for j in range (l+1):
    for i in range (1,l+1):
        
        if k1[i][j] == 1:
            a =  [k1[i][j-1],k1[i-1][j]]
            a.sort()
            if a[1] > a[0] and a[0]!=0 and a[1] != 0:
                k1[i][j] = min(a[0],d)
                np.place(k1, k1 == a[1] ,min(a[0],d))
            elif a[0]!= 0:
                k1[i][j] = a[0]
            elif a[0]==0 and a[1] != 0:
                k1[i][j] = min(a[1],d)
            elif a[1]==0:
                k1[i][j]= d
        else :
            d += 1
for i in range (l+1):
    if k1[i][l]== 1:
        print("khoshe bi nahat be vojod amade , etesal bargharar ast")
    else:
        print ("etesal barghar nist")
k1 = np.delete(k1,0,axis= 0)
k1 = np.delete(k1,0,axis= 1)
k1 = np.delete(k1,l,axis= 1)
plt.imshow(k1%11 )
plt.show()
