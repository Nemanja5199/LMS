import numpy as np


x= np.array([[1,2,-4,5]])

y= np.array([[1],[2],[3],[4]])



x1= np.array([[1,2,3]])
y1= np.array([[1],[2],[3]])
c1=np.dot(x1,y1)


c2=np.outer(x1,y1)
#c2=np.multiply(x1,y1) Vraca isto

#Element po element
c3=np.multiply(x1,x1)

print(np.random.randint(1,5))

