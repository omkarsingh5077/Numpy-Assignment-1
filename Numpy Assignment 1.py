
import pandas as pd
import numpy as np

# # Create a null vector of size 10 but the fifth value which is 1

a= np.zeros(10)
a[4]= 1
print (a)




# # Create a vector with values ranging from 10 to 49

b = np.arange(10,50)
print (b)




# # Create a 3x3 matrix with values ranging from 0 to 8

c = np.arange(9).reshape(3,3)
print (c)





# # Find indices of non-zero elements from [1,2,0,0,4,0]

non_zero = np.nonzero([1,2,0,0,4,0])
print(non_zero)




# # Create a 10x10 array with random values and find the minimum and maximum values.

Z = np.random.random((10,10))
print("original array:",Z)
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)






# Create a random vector of size 30 and find the mean value.


x = np.random.random(30)
print("Original array:",x)
m = x.mean()
print('mean of random vector is :', m)

