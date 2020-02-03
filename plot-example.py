import numpy as np
import matplotlib.pyplot as plt

max = 500000
step = 1.0/1000.0
x = np.arange(0,max)*step
arr = 0.1 * np.round(4. * np.sin(x))/4. + 1 * np.log(1 + x)

T = 1.57 # try 0.1 0.5 1 2 2.5 yourself
# if there is a periodic component, this approach seems to amplify the periodic component
# T up to half of the period seems OK. T above period will have the amplifier effect
# so the approach fit random data such as sales, customer counts, etc
# print('t:', (x[0:int(T/step)] - x[int(T/step)-1]), T)
avg = T * np.sum(arr[0:int(T/step)] * np.exp((x[0:int(T/step)] - x[int(T/step)-1])*T))
res = np.zeros(max)
sum = np.zeros(max)
# print('avg', avg, np.exp(-T*step))
decay = np.exp(-T*step)
for i in np.arange(int(T/step),max):
    avg = avg * decay + T * arr[i]
    res[i] = avg
    sum[i] = np.sum(arr[i-int(T/step):i])/T
    # print(arr[i], avg)

plt.plot(x[400000:500000], arr[400000:500000], 'r--', x[400000:500000], res[400000:500000], 'b--', x[400000:500000], sum[400000:500000], 'g--')
plt.show()
