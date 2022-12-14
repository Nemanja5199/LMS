
import matplotlib.pyplot as plt

import numpy as np


n= np.arange(0,100,1)

x_n = np.exp(0.1*n)


plt.stem(n,x_n)
plt.show()