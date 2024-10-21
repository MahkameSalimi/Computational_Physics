import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.cm as cm
from statistics import mean
from statistics import variance
from statistics import stdev

L = [10, 40,80,100,160 ,200]#lattice sizes
#l=160
for l in L:
#if l == 160:
    QQ =[]
    Q00 = []
    s2=[]
    P1 = [0.1,0.2,0.3,0.4,0.42,0.44,0.46,0.48,0.5,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6, 0.61, 0.62,0.63,0.64,0.65,0.66,0.67,0.7,0.73,0.76,0.8,0.9,1]
    for p in P1:
        Q =[0]
        Q1 =[0]
        s1=np.zeros(100)
        #run 100 times
        for t in range(100):
            #add two column foe easier cheking
            k = np.zeros((l,l))
            k=  np.random.uniform (0,1,(l,l))< p
            k2 = np.ones((l,1))
            k1 = np.concatenate((k2,k),axis = 1)
            k2 = np.zeros((1,l+1))
            k1 = np.concatenate((k2,k1),axis = 0)
            ###################################
            L = np.zeros (l*l)
            S =np.zeros(l*l)
            k1 = k1.astype('int')
            L = L.astype('int')
            S = S.astype('int')
            
            ###############################
            L[1] = 1
            d = 2
            #heshen kopelman
            for j in range (1,l+1):
                for i in range (1,l+1):
                    if k1[i][j] !=0 :
                        a =  [L[k1[i][j-1]],L[k1[i-1][j]]]
                        a.sort()
                        b =  [k1[i][j-1],k1[i-1][j]]
                        if b[0]!=0 and b[1] != 0:

                            k1[i][j] = L[a[0]]
                            if L[a[0]] != L[a[1]]:
                                S[L[a[0]]] =  S[L[a[0]]] + S [L[a[1]]]+1
                                S[L[a[1]]] = 0
                            else :
                                S[L[a[0]]] =  S[L[a[0]]] +1
                            np.place (L, L == L[a[1]] ,L[a[0]])

                        elif b[0]!= 0:
                            k1[i][j] = L[b [0]]
                            m =L[b [0]]
                            S[L[m]] = S[L[m]]+1
                        elif b[0]==0 and b[1] != 0:
                            k1[i][j] = L[b [1]]
                            m = L[b [1]]
                            S[L[m]] =  S[L[m]]+1
                        elif b[1]==0:
                            L[d] = d
                            k1[i][j]= L[d]
                            m = L[d]
                            S[L[m]] =  S[L[m]]+1
                            d += 1
            # replace all the L                
            for j in range (1,l+1):
                for i in range (1,l+1):
                    if k1[i][j] != 0:
                        k1[i][j] = L[k1[i][j]]
            #Q mean
            if np.any(k1[:,l]==1):
                Q.append(1)
                flag = 0
                while flag != 1:
                    i = int(np.random.randint(1,l+1))
                    j = int(np.random.randint(1,l+1))
                    if k1[i][j] != 0:#choose on sites
                        flag = 1
                #q infinity
                if k1[i][j] == 1 :
                    Q1.append(1)
                else :
                    Q1.append(0)
                    
            else :
                Q.append(0)
    ##############################################
            ##instead of correlation length we use sqrt(s)
            S = S[S!=0]
            S.sort()
            s10 = S
            sums = np.sum(S)
            ps = []

            for i in s10:
                ps.append(np.count_nonzero(s10==i))
                s10 = s10[s10!=i]

            ps = np.array(ps)
            ps =ps[ps != 0]

            S = np.unique(S)
            Ps =[]
            q = 0
            for i in S:

                Ps.append((ps[q]*i)/sums)
                q = q+ 1   
            S = np.unique(S)
            #probibility of S
            Ps = np.array(Ps)
    #########################################################

            if np.any(k1[:,l]==1):
                S = S[S!=max(S)]
                Ps = Ps[:(len(S))]
                if len(S)!=0 and np.sum(Ps)==1:
                    #choose random between on sites with difinite probiblity
                    s1[t] = np.sqrt(float(np.random.choice(S,p =Ps)))

            else:
                if len(S)!=0 and np.sum(Ps)==1:
                    s1[t] = np.sqrt(float(np.random.choice(S,p= Ps)))
        #mean value after 100 runs
        s2.append(np.mean(s1))
        QQ.append (mean(Q))
        Q00.append (mean(Q1))


    p.savetxt ( 'qmean'+str(l)+'.txt',QQ)
    np.savetxt ( 'Qinf'+str(l)+'.txt',Q00)
    np.savetxt ( 'corr'+str(l)+'.txt',s2)
    print(l)
#plot delta p - L
np.savetxt ( "p0.txt",P1)
ss_10 = np.loadtxt("corr10.txt")
ss_40 = np.loadtxt("corr40.txt")
ss_80 = np.loadtxt("corr80.txt")
ss_100 = np.loadtxt("corr100.txt")
ss_200 = np.loadtxt("corr10.txt")
p0 = np.loadtxt("p0.txt")
############################################################
#plot correlaton lenght
im1 = plt.plot(p0,ss_10,'.-')
im2 = plt.plot(p0,ss_40,'.-')
im3 = plt.plot(p0,ss_80,'.-')
im4 = plt.plot(p0,ss_100,'.-')
im5 = plt.plot(p0,ss_200,'.-')
plt.legend(['L =10',' L = 40' ,' L = 80',' L= 100' , 'L = 200'], loc = 'upper left')
plt.xlabel(" P")
plt.ylabel("sqrt(s)")
plt.show()
P1[np.argmax(ss_10)]
############################################################
#plot q mean
qq_10 = np.loadtxt("qmean10.txt")
qq_100 = np.loadtxt("qmean100.txt")
qq_200 = np.loadtxt("qmean200.txt")
P0 = np.loadtxt("p1.txt")

im1 = plt.plot(P1,qq_10,'o-')
im2 = plt.plot(P1,qq_100[1:],'.-')
im3 = plt.plot(p0,qq_200,'.-')
plt.legend(['L =10',' L= 100' , 'L = 200'], loc = 'upper left')
plt.xlabel(" P")
plt.ylabel(" Q mean")
plt.show()
###################################################
#plot q infinity
q00_10 = np.loadtxt("Qinf10.txt")
q00_100 = np.loadtxt("Qinf100.txt")
q00_200 = np.loadtxt("Qinf200.txt")
np.savetxt ( "p1.txt",P1)
p0 = np.loadtxt("p0.txt")
im1 = plt.plot(P1,QQ,'o-')
im2 = plt.plot(P1,q00_100[1:],'o-')
im3 = plt.plot(p0,q00_200,'o-')
plt.legend(['L =10',' L= 100' , 'L = 200'], loc = 'upper left')
plt.xlabel(" P")
plt.ylabel(" Q infinity")

plt.show()


#fitting data and fine no
delta_p = [P1[np.argmax(ss_10)],P1[np.argmax(ss_40)],P1[np.argmax(ss_80)],P1[np.argmax(ss_100)],0.6]
delta_p = np.array(delta_p)
pc = 0.59
delta = np.log(abs(delta_p - pc))
L = np.log(np.array([10, 40,80,100,200]))
m = np.polyfit(L , delta ,1)
print ("m =",m[0])
plt.plot (L,delta,'o' , L,L*m[0]+m[1])
plt.xlabel(" L ")
plt.ylabel("delta_P")
plt.show()

