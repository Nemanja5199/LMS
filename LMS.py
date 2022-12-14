import numpy as np
import matplotlib.pyplot as plt
import random
# Generated signal
t= np.arange(0.001,1,0.001)
D= 2*np.sin(2*np.pi*10*t)

# Generated signal with noise
n= np.size(D)
sum=0.0008*np.asarray(random.sample(range(0,n),n)) 
A= D[:n] + sum


M=25
w= np.ones(M)
wi=np.ones(M)
E=np.ones(n)
mu=0.0005

for i in range(M,n):
    E[i]=D[i] - np.dot(wi,np.transpose(A[i:i-M+1:-1]))
    print(E[i])
    wi= wi+ 2*mu*np.dot(E[i],A[i:i-M+1:-1])

# Estimate signal
Est= np.ones(n)
for i in range(M+1,n):
    j=A[i:i-M+1:-1]
    Est[i]= np.dot(wi,np.transpose(j))

# Calculate signal error
Err= Est - D

# Display signals
plt.subplot(4,1,1)
plt.title('Desired signal')
plt.plot(D)
plt.subplot(4,1,2)
plt.title('Signal with noise')
plt.plot(A)
plt.subplot(4,1,3)
plt.title('Estimated signal')
plt.plot(Est)
plt.subplot(4,1,4)
plt.title('Signal error')
plt.plot(Err)
plt.show()
