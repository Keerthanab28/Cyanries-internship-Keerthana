import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)

arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)

print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr.shape)
print(arr1.shape)
print(arr2.shape)
print(arr.itemsize)
print(arr1.itemsize)
print(arr1.nbytes)
print(arr2.itemsize)
print(arr2.nbytes)


# VECTORISED OPERATIONS


numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(numbers +5)
print(numbers - 5)
print(numbers * 2)
print(numbers / 2)
print(numbers ** 2)
print(numbers % 2)
print(numbers // 2)

print(np.sqrt(numbers))
print(np.exp(numbers))

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))
print(np.cos(angles))
print(np.tan(angles))

r = np.array([12,20,51,7,8,700])
print(np.max(r))
print(np.min(r))
print(np.mean(r))
print(np.std(r))


print(r > 10)
print(r < 10)


are = np.array([10,20,30,40,50])

print(are[are > 20])
print(are[are < 20])

print(are[(are > 20) & (are < 50)])

print(np.mean(are))
print(np.median(are))
print(np.sum(are))
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.sum(matrix , axis = 0))
print(np.prod(matrix , axis = 0))

print(np.sort(matrix))
print(np.sort(are))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))

print(np.vstack((a,b,a)))
print(np.hstack((a,b,a)))

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.reshape(2, 3))


# broadcasting


at = np.array([10,20,30,40,50])


mat = np.array([[1,2,3,4,4],[5,6,7,8,9]])

print(at + 10)
print(at + mat)

# BROADCASTING

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print("Matrix:")
print(matrix)

print("\nVector:")
print(vector)

print("\nBroadcasting - Addition:")
print(matrix + vector)

print("\nBroadcasting - Multiplication:")
print(matrix * vector)

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A * B)
print(A @ B)

import pandas as pd

data = pd.read_csv(r'C:\\Users\\keert\\OneDrive\\Desktop\\Cyanries-internship-Keerthana\\Week-1\\numpy\\data\\iris.csv')
print(data)
print(data.head(5))
print(data.dtypes)
print(data.info())
print(data.describe())
numeric_data = data.select_dtypes(include=np.number)

print(numeric_data.head())

numeric_array = numeric_data.to_numpy()
print(numeric_array)

mean_values = np.mean(numeric_array, axis = 0)
print("\nMean values:")
print(mean_values)
median_values = np.median(numeric_array, axis = 0)
print("\nMedian values:")
print(median_values)
sum_values = np.sum(numeric_array, axis = 0)
print("\nSum values:")
print(sum_values)
standard_deviation = np.std(numeric_array, axis = 0)
print("\nStandard deviation:")
print(standard_deviation)

correlation_matrix = np.corrcoef(numeric_array, rowvar = False)
print("\nCorrelation matrix:")
print(correlation_matrix)

