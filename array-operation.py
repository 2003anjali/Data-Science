import numpy as np
#create arrays
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

#Basic Operations
print("Array a : ",a)
print("Array b : ",b)
print("Sum of arrays a and b : ",np.add(a,b))
print("Difference of arrays of a and b : ",np.subtract(a,b))
print("Product of arrays of a and b : ",np.multiply(a,b))
print("Division of arrays of a and b : ",np.divide(a,b))
print("Square root of array of a : ",np.sqrt(a))
print("Exponential of array of a : ",np.exp(a))

#Aaggregation operations
print("Minimum value of array of a : ",np.min(a))
print("Maximum value of array of b : ",np.max(b))
print("Mean of array of a : ",np.mean(a))
print("Standard deviation of array of b : ",np.std(b))
print("Sum of elements of array a : ",np.sum(a))

#reshaping arrays
c=np.array([[1,2],[3,4],[5,6]])
print("Array c : ")
print(c)
print("Reshaped array c(2 rows, 3 columns):")
print(np.reshape(c,(2,3)))

#Transposing arrays
d=np.array([[1,2,3],[4,5,6]])
print("Array d: ")
print(d)
print("Transposed array d: ")
print(np.transpose(d))