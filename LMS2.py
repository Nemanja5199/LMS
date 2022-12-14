import numpy as np
import matplotlib.pyplot as plt

# define the LMS function
def LMS(x, d, mu, w):
  # initialize the error to zero
  e = 0
  
  # update the weights
  w = w + 2*mu*e*x
  
  # calculate the error
  e = d - w.T @ x
  
  return w, e

# set the initial weights to zero
w = np.zeros((1, 3))

# set the input and desired output
x = np.array([1, 2, 3])
d = 2

# set the learning rate
mu = 0.1

# transpose the weights to match the dimensions of the input
w = w.T

# run the LMS algorithm
w, e = LMS(x, d, mu, w)

# reshape the error to match the dimensions of the weights
e = e.reshape(1, 3)

# plot the input and desired output
plt.plot(x, d * np.ones(x.shape), 'ro')

# plot the final weights and error
plt.plot(w[0,:], e[0,:], 'bo')
plt.show()
