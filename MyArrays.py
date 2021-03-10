#
#
#
import numpy as np

"""
integers = np.array([1, 2, 3])

print(type(integers))
print(integers)


# create one demnsional array from a list comprehension that produces even integers from 2 through 20
# EXERCISE
integers = np.array([x for x in range(2, 21, 2)])
print(integers)


integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size


print()


for row in integers:
    print(type(row))
    print(row)
    for col in row:
        print(col, end=" ")

# itrates through all values disregarding columns and rows
for i in integers.flat:
    print(i)

"""
##EXERCISE
import random

array12 = np.array(
    [
        [random.randint(1, 10) for i in range(5)],
        [random.randint(1, 10) for i in range(5)],
    ]
)

print(array12)

array21 = np.array(np.random.randint(1, 10, size=(2, 5)))
print(array21)


c = np.zeros(5)  # create an array of 5 elements of zeros

print(np.ones(5))  # create an array of 5 elements of 1s

print(np.ones((2, 4), dtype=int))  # create an array of 2 by 4 of ones of type int

print(np.full((3, 5), 13))  # create an array of 3 rows of 5 columns of the number 13

print(np.arange(5))  # like the range function, using integers

print(np.arange(5, 10))  # includes lower limit but not upper limit

print(np.arange(10, 1, -2))  # step value for descending order

print(np.linspace(0.0, 1.0, num=5))  # evenly spaced float range

array1 = np.arange(1, 21)

array2 = array1.reshape(4, 5)

print(array1)

print(array2)


array3 = np.arange(1, 100001).reshape(4, 25000)

print(array3)

array4 = np.arange(1, 100001).reshape(100, 1000)

print(array4)

numbers = np.arange(1, 6)

numbers += 10

print(numbers)


# broadcasting

print(numbers * 2)
print(numbers ** 3)


print(numbers)


numbers2 = np.linspace(1.1, 5.5, 5)

a = numbers * numbers2

print(a)


# comparing arrays

print(numbers >= 13)

print(numbers2 < numbers)

print(numbers == numbers2)
