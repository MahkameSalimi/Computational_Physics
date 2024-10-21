import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev
from statistics import mean
from datetime import datetime
from statistics import variance
start_time = datetime.now()
# do your work here

f1 = []
f2 = []
for i in range(1000000):
    x1 = np.random.uniform(-1,1)
    x = np.random.uniform(0,1)
    
    f1.append((x1*x+3)*x**3*x1)
    f2.append((x1*x+3)*x**2)
    
fmean1 = mean(f1)
fmean2 = mean(f2)
I1 = (1-0)*(1-(-1))*(fmean1)
I2 = (1-0)*(1-(-1))*(fmean2)
I =I1/I2
print (I, '\n' )

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

error1 = np.sqrt(variance (f1))/np.sqrt(1000000)
error2 = np.sqrt(variance (f2))/np.sqrt(1000000)
error = -I *(error1/I1 + error2/I2)
print(error)
