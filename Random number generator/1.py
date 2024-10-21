import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from datetime import datetime
from statistics import variance
#run time
start_time = datetime.now()


f = []

for i in range(1000000):
    x = np.random.uniform(0,2)
    f.append(np .exp (-x**2))
    
fmean = mean(f)
I = (2-0)*(fmean)

print (I)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

error = np.sqrt(variance (f))/np.sqrt(1000000)

#========================================================================

#inteligant

import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev
from statistics import mean
from datetime import datetime
from statistics import variance
start_time = datetime.now()

#g(x)=exp(-x)

f2 = []
n=0
while n<1000000:

        #choose a number between 0 , 2

    y = np.random.uniform (0,1)

    x =(-np.log(y))
    if x>0 and x<2 :
        n += 1
        f2.append(np .exp (-x**2+x))
             
             
fmean = mean(f2)
I_g = -(np.exp(-2)-1)

I = I_g*(fmean)

print ("error =", error ,'\n', I,'\n', n)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
error2 = np.sqrt(variance (f2))/np.sqrt(100000)
print (error2)
                 
