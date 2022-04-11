from gettext import npgettext
import numpy


import numpy as np
print("creating an array and dimension of an array ")

z = np.array([
    [2, 3],
    [5, 7]
]
)
y = np.array([1, 2, 3, 4, 5])
x = np.array([
    [1, 2, 3],
    [4, 5, 6]])

w = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ], [
        [1, 2, 3],
        [4, 5, 6]

    ]]
)

print(z.ndim)
print("----------------------")

print(y.ndim)
print("----------------------")

print(x.ndim)
print("----------------------")

print(w.ndim)

print("#############################################")
a = np.ones((2, 3))
print( "ones",a)
print("----------------------")

e = np.zeros(4)
print("zeros",e)
print("----------------------")

b = np.arange(2, 7, 2)
print("----------------------")

print("arrange",b)
print("----------------------")

c = np.concatenate([[2, 5, 7, 8], [1, 3, 5, 7]], axis=0)
print("concatenate",c)
print("----------------------")

d = a.astype(int)
print("astype",d)
print("----------------------")

f = np.zeros_like(c)
print("zeros_like",f)
print("----------------------")

g = np.ones_like(c)
print("ones_like",g)
print("----------------------")

i = np.random.random(size=4)
print("random.random",i)
print("----------------------")

j = np.random.randint(7, size=4)
print("random.randint",j)
#############################################
print("transpose ----- and reshaping")
transposed_array = np.transpose([[0, 1], [2, 3]])
print("transposed_array",transposed_array)
print("----------------------")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 33])
newArray = arr.reshape(4, 3)

print("rashape an array",newArray)
print("----------------------")

# newArray_2 = arr.reshape(4,4)

# print(newArray_2)
# print("----------------------")

newArray_3 = arr.reshape(2, 2, -1)
print("rashape(2,2,-1)",newArray_3)

print("flatten ----")

threeDimensionArray = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ], [
        [1, 2, 3],
        [4, 5, 6]

    ]]
)
flattendArray = threeDimensionArray.flatten()

print("flatten",flattendArray)

print("indexing an array")

randomArray = np.random.randint(5, size=(3, 4, 5))

print(randomArray)
print(randomArray[0][0][0])
print(randomArray[1, 2, 3])
print(randomArray[-1, -1][-1])
print("mathematical oprations")

arrayToExcute_1 = np.random.randint(5, size=(2, 3))
arrayToExcute_2 = np.random.randint(9, size=(2, 3))

print(arrayToExcute_1)
print(arrayToExcute_2)
print("---------------------")
addedArrays = np.add(arrayToExcute_1, arrayToExcute_2)
print("addition",addedArrays)

subtractedArray = np.subtract(arrayToExcute_1, arrayToExcute_2)

print("subtruction",subtractedArray)

multiplyArray = np.multiply(arrayToExcute_1, arrayToExcute_2)

print("multiplication",multiplyArray)

dividedArray = np.divide(arrayToExcute_1, arrayToExcute_2)
print("division",dividedArray)

poweredArray = np.power(arrayToExcute_1, arrayToExcute_2)

print("powered",poweredArray)

modArray = np.mod(arrayToExcute_1, arrayToExcute_2)
print(modArray)

print("adding arrays with different dimension")
arrayToExcute_3 = np.random.randint(5, size=(3, 3))
arrayToExcute_4 = np.random.randint(9, size=(2, 3))
print(arrayToExcute_3)
print(arrayToExcute_4)

# addedArraysWithDifferentDimension = np.add(arrayToExcute_3,arrayToExcute_4)
# print(addedArraysWithDifferentDimension)
print("dot product of arrays and dot product of vector")


newArray_5 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])


newArray_6 = np.array([[2, 3, 4], [5, 6, 7],
                       [8, 9, 10]])


print("---------------------")

print(newArray_5)
print(newArray_6)
print("---------------------")
o = np.matmul(newArray_5, newArray_6)
o1 = np.dot(newArray_5,newArray_6) 
o2 = np.vdot(newArray_5,newArray_6) 

print("matrix product",o)
print(" array dot product",o1)
print("vector dot product",o2)
