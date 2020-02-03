import numpy as np

# set the total number of points as 50000
k = 50000
arr = np.ones(k)

s1 = 1
s2 = 3
s3 = 6
s4 = 24

# -np.arange(0, k) will product array from 0, -1, -2, ...., -k
at1 = s1 * np.sum(arr * np.exp(-np.arange(0, k)*s1))
at2 = s2 * np.sum(arr * np.exp(-np.arange(0, k)*s2))
at3 = s3 * np.sum(arr * np.exp(-np.arange(0, k)*s3))
at4 = s4 * np.sum(arr * np.exp(-np.arange(0, k)*s4))

# here you can see the average
print('average over 1 day:', at1)
print('average over 3 day:', at2)
print('average over 6 day:', at3)
print('average over 24 day:', at4)

# average over 1 day: 1.5819767068693265
# average over 3 day: 3.1571870894737675
# average over 6 day: 6.014909469941067
# average over 24 day: 24.000000000906034
