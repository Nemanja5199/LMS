import numpy as np
import matplotlib.pyplot as plt
import random
# Generated signal
t= np.arange(0.001,1,0.001)
D= 2*np.sin(2*np.pi*20*t)

# Generated signal with noise
n= np.size(D)
#sum=0.0009*np.asarray(random.sample(range(0,n),n)) 
ma, sigma = 4, 3.5
sum= 0.09*np.random.normal(ma, sigma, 999)
A= D[:n] + sum

print(A)
print('_____________')
print(D)

M=25
w= np.zeros(M)
wi=np.zeros(M)
E=np.zeros(n)
mu=0.0005

for i in range(M+1,n):
    E[i]=D[i] - np.dot(wi,A[i:i-M:-1])
    wi= wi+ 2*mu*E[i]*A[i:i-M:-1]

# Estimate signal
Est= np.zeros(n)
for i in range(M+1,n):
    j=A[i:i-M:-1]
    Est[i]= np.dot(wi,j)

# Calculate signal error
Err= np.transpose(Est) - D

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

