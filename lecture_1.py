#formula for etterspørsel
# P = c - dX^D

import numpy as np 
import matplotlib.pyplot as plt 
def P(c,d,D):
    return c - d*X**D

X = np.arange(20)
D = 2.0 
d = 0.5
c = 300 

plt.plot(X,P(c,d,D))
plt.show()



