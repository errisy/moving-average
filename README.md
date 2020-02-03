# moving-average
the moving average computation with Laplace transform

```python
import numpy as np

k = 50000
arr = np.ones(k)

s1 = 1
s2 = 3
s3 = 6
s4 = 24

at1 = s1 * np.sum(arr * np.exp(-np.arange(0, k)*s1))
at2 = s2 * np.sum(arr * np.exp(-np.arange(0, k)*s2))
at3 = s3 * np.sum(arr * np.exp(-np.arange(0, k)*s3))
at4 = s4 * np.sum(arr * np.exp(-np.arange(0, k)*s4))

print('average over 1 day:', at1)
print('average over 3 day:', at2)
print('average over 6 day:', at3)
print('average over 24 day:', at4)

```
