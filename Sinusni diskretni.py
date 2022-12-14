

import numpy as np
import matplotlib.pyplot as plt

n= np.arange(0,1,0.01)
xn=np.sin(2*np.pi*3*n)
plt.stem(n,xn)
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()





