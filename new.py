import numpy as np
def guess_what(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]
    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]
    return z

c = np.arange(9).reshape(3,3)
d = np.arange(3).reshape(3,1)

print(guess_what(c,d))