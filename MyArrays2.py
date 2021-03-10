import numpy as np



grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# rows - grades for eah student
# cols- grades for each test


a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)
print("Average of each Test:", g)


h = grades.mean(axis=1)
print("Average of each Student:", h)


# axis=0 by column for each test
# axis=1 by row for each student

numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)
print(sqrt)


numbers2 = np.arange(1, 7) * 10

add = np.add(numbers, numbers2)

print(add)

multiply = np.multiply(numbers2, 5)
print(multiply)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

multiply2 = np.multiply(numbers3, numbers4)

print(multiply2)

 this works because numbers4 has the same length as each row of numbers3,
so NumPy can apply the multiply operation by treating numbers4 as if it were the 
following array:


array([[2, 4, 6],
[2, 4, 6]])  

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

a = grades[0, 1]
print(a)


b = grades[1]
print(b)

# to select multiple sequential rows
# notation (remember upper limit is not included):
firsttwo = grades[0:2]
print(firsttwo)


# to select multiple non-sequential rows, use a list of row indices:
grades[[1, 3]]


# all rows and only first column
c = grades[:2, 0]
print(c)


# you can select consecutive columns using a slice
d = grades[:, 1:3]
print(d)

# or specific columns using a list of column indices:
e = grades[:, [0, 2]]
print(e)


import random

grades = np.random.randint(60, 101, 12).reshape(3, 4)

print(grades.mean())

print(grades.mean(axis=0))

print(grades.mean(axis=1))

#########################
numbers = np.arange(1, 6)

numbers2 = numbers.view()

numbers[1] *= 10
print(numbers2)


numbers2[1] /= 10
print(numbers)


numbers2 = numbers[0:3]


numbers[1] *= 20
print(numbers2)


# deep copies
# creates new independent array
numbers = np.arange(1, 6)
numbers2 = numbers.copy()


numbers[1] *= 10
print(numbers)
print(numbers2)


# the array methods reshape and resize both enable you to change an arrays dimensions.
# method reshape returns a view of the original array with the new dimensions. It does not modify the original array

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1, 6)

print(a)
print(grades)


b = grades.resize(1, 6)
print(grades)


flattened = grades.flatten()


raveled = grades.ravel()

raveled[0] = 100
raveled[5] = 99

print(grades)

# transpose an arrays rows and columns-that is "flip" the array
# so the rows become the columns and the columns become the rows
# the t attribute returns a transposed view of the array

transposed = grades.T

print(transposed)



grades = np.array([[87, 96, 70], [100, 87, 90]])
grades2 = np.array([[94, 77, 90],[100, 81, 82]])

h_grades = np.hstack((grades, grades2))


print(h_grades)

print(grades)

v_grades = np.vstack((grades, grades2))
print(v_grades)