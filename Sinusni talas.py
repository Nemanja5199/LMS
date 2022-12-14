

import numpy as np
import matplotlib.pyplot as plt

t= np.arange(0,1,0.001)
xt=np.sin(2*np.pi*5*t)
plt.plot(t,xt)
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()





