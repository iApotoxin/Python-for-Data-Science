# -*- coding: utf-8 -*-
"""numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JP1SN3laSc617o3A8UVDACGZR-Sh8Asm

**NumPy(Numeric Python) เป็น module ของ Python ที่มีฟังก์ชั่นด้านคณิตศาสตร์ และการจัดการกับชุดข้อมูลขนาดใหญ่อย่าง Array Vector และ Matrix

Arrays สามารถดำเนินกับข้อมูลเชิงตัวเลขได้รวดเร็วและมีประสิทธิภาพดีกว่า List เราจะนำ Array มาใช้ในการสร้าง Vectors และ Matric
**

Array 1 มิติ = Vectors

Array 2 มิติ = Matrics

.array จะใช้รับค่า หรือ List ที่เราจะเอามาสร้างเป็น Array
"""

import numpy as np

myNum = np.arange(10)
print('Element of myNum : ', myNum)
print(type(myNum))

print("--------------------------------------------------------------")

myList = list(range(10))
print('Element of myList : ', myList)
print(type(myList))

print("--------------------------------------------------------------")

myArray = np.array(np.arange(10))
print('Element of myArray : ', myArray)
print(type(myArray))

# Creating ndarrays
# Convert Lit to Array

arr1 = np.array([10,20,30,40])
print(arr1)
print(type(arr1))
print(arr1.dtype)

# Creating ndarrays
# Convert Lit to Array and Covent Element Type
# Convert integer to float

arr2 = np.array([10,20,30,40],float) 
print(arr2)
print(type(arr2))
print(arr2.dtype)

print("--------------------------------------------------------------")

print(arr2[0])
print(arr2[1])
print(arr2[2])
print(arr2[3])

print("--------------------------------------------------------------")
#Assign Value to Array

arr2[0]=50   # Auto Covert int to float
print(arr2)
print(arr2.dtype)

## Creating ndarrays

data1 = [6, 7.5, 8, 0, 1]
arr3 = np.array(data1)
print(arr3)
print(arr3.dtype)

print("--------------------------------------------------------------")

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr4 = np.array(data2)
print(arr4)
print(arr4.dtype)

arr5 = np.array([[10,20,30],[40,50,60]],float)
print(arr5)
print(type(arr5))
print(arr5.dtype)

print("--------------------------------------------------------------")

print(arr5[0,0])
print(arr5[0,1])
print(arr5[0,2])

print(arr5[1,0])
print(arr5[1,1])
print(arr5[1,2])

print(arr5.ndim)     # show dimensions of array

print(arr5.shape)

# Random Function

data = np.random.randn(3, 4)
print(data)

print("--------------------------------------------------------------")

print(data.shape)
print(data.dtype)

print("--------------------------------------------------------------")

print(data + data)

print("--------------------------------------------------------------")

print(data * 10)

print(np.ones(10))

print("--------------------------------------------------------------")

print(np.ones((5, 6)))

print(np.zeros(10))

print("--------------------------------------------------------------")

print(np.zeros((3, 6)))

print(np.arange(15))

"""**Data Type**

int8, uint8 |
int16, uint16 |
int32, uint32 |
int64, uint64 |
float16 | float32 | float64 | float128 |
bool | object | string_ | unicode_
"""

arr6 = np.array([1, 2, 3, 4, 5])
print(arr6.dtype)

print("--------------------------------------------------------------")

float_arr = arr6.astype(np.float64)

print(float_arr)
print(float_arr.dtype)

arr7 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr7)

print("--------------------------------------------------------------")

print(arr7.astype(np.int32))

numeric_unicode = np.array(['1.25', '-9.6', '42'])   # U --> Unicode_
print(numeric_unicode)
print(numeric_unicode.dtype)

print("--------------------------------------------------------------")

numeric_float = numeric_strings.astype(float)
print(numeric_float)
print(numeric_float.dtype)

print("--------------------------------------------------------------")

numeric_strings = np.array(['1.25', '-9.6', '42'],dtype=np.string_)   # S --> String_
print(numeric_strings)
print(numeric_strings.dtype)

print("--------------------------------------------------------------")

num_float = np.array(['1.25', '-9.6', '42'],dtype=np.float64)   
print(num_float)
print(num_float.dtype)

print("--------------------------------------------------------------")

#num_int = np.array(['1.25', '-9.6', '42'], dtype=np.int64)   
#print(num_int)
#print(num_int.dtype)

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)

change_arr = int_array.astype(calibers.dtype)

print(int_array.dtype)
print(change_arr)
print(change_arr.dtype)

"""**Arithmetic with NumPy Arrays**"""

arr8 = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr8)

arr9 = np.array([[0., 4., 1.], [7., 2., 12.]])
print (arr9)

print("--------------------------------------------------------------")

print(arr8 + arr8)

print("--------------------------------------------------------------")

print(arr8 - arr8)

print("--------------------------------------------------------------")

print(arr8 * arr8)

print("--------------------------------------------------------------")

print(arr8 / arr8)

print("--------------------------------------------------------------")

print(1 / arr8)

print("--------------------------------------------------------------")

print(arr8 ** 2)

print("--------------------------------------------------------------")

print(arr9 > arr8) # compare value by value

"""**Basic Indexing and Slicing**"""

arr10 = np.arange(10)
print(arr10)

print("--------------------------------------------------------------")

print('arr10[5] : ',arr10[5])
print('arr10[5:8] : ',arr10[5:8])

print("--------------------------------------------------------------")

arr10[5:8] = 12
print(arr10)

arr11 = np.arange(10)
print(arr11)

print("--------------------------------------------------------------")

arr_slice = arr11[5:8]
print(arr_slice)

print("--------------------------------------------------------------")

arr_slice[1] = 600
print(arr11)

print("--------------------------------------------------------------")

arr_slice[:] = 100
print(arr11)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d[0])
print(arr2d[1])
print(arr2d[2])

print("--------------------------------------------------------------")

print(arr2d[0][2])

print("--------------------------------------------------------------")

print(arr2d[0, 2])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)

print("--------------------------------------------------------------")

print(arr3d[0])
print(arr3d[1])

print("--------------------------------------------------------------")

arr3d[0] = 50
print(arr3d)

arr12 = np.array([0,1,2,3,4,100,100,100,8,9])
print(arr12)

print(arr12[1:6])

print("--------------------------------------------------------------")

print(arr12[:3])

print("--------------------------------------------------------------")

print(arr12[::2])

arr13 = np.array([[1, 2, 3] , [4, 5, 6] , [7, 8, 9]])
print(arr13)

print("--------------------------------------------------------------")

print(arr13[:2, 1:])

print("--------------------------------------------------------------")

"""**Boolean Indexing**"""

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names)

print("--------------------------------------------------------------")

dataA = np.random.randn(7, 4)
print(dataA)

print("--------------------------------------------------------------")

print(names == 'Bob')

print("--------------------------------------------------------------")

print(dataA[names == 'Bob'])   #dataA[0] , data[3]

print("--------------------------------------------------------------")

print(dataA[names == 'Bob', 2:])  # [0,2:] , [3,2:]

print("--------------------------------------------------------------")

print(dataA[names == 'Bob', 3])  # [0,3] , [3,3]

print("--------------------------------------------------------------")

print(names != 'Bob')

print("--------------------------------------------------------------")

print(dataA[~(names == 'Bob')])

print("--------------------------------------------------------------")

cond = names == 'Bob'
print(dataA[~cond])

mask = (names == 'Bob') | (names == 'Will')  
print(mask)

print("--------------------------------------------------------------")

print(dataA)

print("--------------------------------------------------------------")

print(dataA[mask])  # 0,2,3,4

dataA[dataA < 0] = 0   # จำนวนลบ (น้อยกว่า 0) ถูกแทนด้วย 0
print(dataA)

dataA[names != 'Joe'] = 7
print(dataA)

"""**Fancy Indexing**"""

arr14 = np.empty((8, 4))

for i in range(8):
  arr14[i] = i

print(arr14)

arr15 = np.arange(32).reshape((8, 4))
print(arr15)

"""**Transposing Arrays and Flatten**"""

arrayA = np.array([[1,2,3],[4,5,6]],float)
print(arrayA)

print("--------------------------------------------------------------")

arrayB = arrayA.transpose()
print(arrayB)

# Arrayหลายมิติสามารถทาให้เหลือมิติเดียวได้โดยใช้ฟังก์ชันflatten()

arrayC = np.array([[1,2,3],[4,5,6]],float)
print(arrayC)

print("--------------------------------------------------------------")

print(arrayC.flatten())

"""**Universal Functions: Fast Element-Wise Array Functions**"""

# ฟังก์ชัน arange คล้ายกับฟังก์ชัน range แต่คืนค่าเป็น array

arrayD = np.arange(5,dtype=float)
print(arrayD)

print("--------------------------------------------------------------")

arrayE = np.arange(1,6,2,dtype=float)
print(arrayE)

arr16 = np.arange(10)
print(arr16)

print("--------------------------------------------------------------")

print(np.sqrt(arr16))  # square root

print("--------------------------------------------------------------")

print(np.exp(arr16))  # exponent

x = np.random.randn(8)
y = np.random.randn(8)

print(x)
print(y)

print("--------------------------------------------------------------")

print(np.maximum(x, y))

a1 = np.array([2,4,3],float)

print(a1.sum())    #หาผลรวม
print(a1.prod())   #หาผลคูณ

a2 =np.array([[0,-2],[3,-1],[3,-5]],float)

print(a2.sum())

#modf Function

arr17 = np.random.randn(7) * 5
print(arr17)

print("--------------------------------------------------------------")

remainder = np.modf(arr17)
print(remainder)

print("--------------------------------------------------------------")

xR , yR = np.modf(arr17)
print(xR)
print(yR)

arr18 = np.array([5,3,9],float)

print(arr18.max())
print(arr18.min())
print(arr18.argmax())    # argmax() ฟังก์ชันสาหรับการหาตาแหน่งของค่าที่มากที่สุด
print(arr18.argmin())    # argmin() ฟังก์ชันสาหรับการหาตาแหน่งของค่าที่น้อยที่สุด

arr19 = np.array([6,4,8,2,9],float)
arr20 = sorted(arr19)

print(arr20)

"""**Array-Oriented Programming with Arrays**"""

#The np.meshgrid function takes two 1D arrays and produces two 2D matrices corresponding to all pairs of (x, y) in the two arrays

points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)
print(ys)

print("--------------------------------------------------------------")

z = np.sqrt(xs ** 2 + ys ** 2)
print (z)

print("--------------------------------------------------------------")

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray); 
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [(x if c else y)
  for x, y, c in zip(xarr, yarr, cond)]

print(result)

result = np.where(cond, xarr, yarr)
print(result)

arr21 = np.random.randn(4, 4)
print(arr21)

print("--------------------------------------------------------------")

print(arr21 > 0)

print("--------------------------------------------------------------")

print(np.where(arr21 > 0, 2, -2))

print("--------------------------------------------------------------")

print(np.where(arr21 > 0, 2, arr21))

"""**Mathematical and Statistical Methods**"""

arr22 = np.array([[0,-2],[3,-1],[3,-5]],float)
print(arr22)

print("--------------------------------------------------------------")

print(arr22.mean(axis=0))     # แนวตั้ง

print("--------------------------------------------------------------")

print(arr22.mean(axis=1))     # แนวนอน

print("--------------------------------------------------------------")

print(arr22.max(axis=0))

print("--------------------------------------------------------------")

print(arr22.max(axis=1))

print("--------------------------------------------------------------")

print(arr22.min(axis=0))

print("--------------------------------------------------------------")

print(arr22.min(axis=1))

arr23 = np.random.randn(5, 4)
print(arr23)

print("--------------------------------------------------------------")

print(arr23.mean())
print(np.mean(arr23))

print("--------------------------------------------------------------")

print(arr23.sum())
print(arr23.sum()/20)   # test mean

arr24 = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr24)

print("--------------------------------------------------------------")

print(arr24.cumsum())  #compute sum down the rows

arr25 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr25)

print("--------------------------------------------------------------")

print(arr25.cumsum(axis=0)) # แนวตั้ง

print(arr25)

print("--------------------------------------------------------------")

print(arr25.cumsum(axis=1))

print(arr25)

print("--------------------------------------------------------------")

print(arr25.cumprod(axis=0))

print(arr25)

print("--------------------------------------------------------------")

print(arr25.cumprod(axis=1))

arrStat = np.array([2,4,9],float)

print(arrStat.mean())
print(arrStat.var())  # variance
print(arrStat.std())  # standard deviation

"""**Methods for Boolean Arrays**"""

arr26 = np.random.randn(10)
print(arr26)

print("--------------------------------------------------------------")

print((arr26 > 0).sum())

bools = np.array([False, False, False, True])
print(bools)

print("--------------------------------------------------------------")

print(bools.any())   # any ใช้ทดสอบว่าหนึ่งค่าหรือมากกว่าในอาร์เรย์เป็นจริง

print("--------------------------------------------------------------")

print(bools.all())  # all ใช้ตรวจสอบว่าทุกค่าเป็นจริง

print("--------------------------------------------------------------")

bools2 = np.array([True, True, True, True])
print(bools2.all())

"""**Sorting**"""

arr27 = np.random.randn(5)
print(arr27)

print("--------------------------------------------------------------")

arr27.sort()
print(arr27)

arr28 = np.random.randn(5, 3)
print(arr28)

print("--------------------------------------------------------------")

arr28.sort(0)  # แนวตั้ง
print(arr28)

print("--------------------------------------------------------------")

arr28.sort(1) # แนวนอน
print(arr28)

"""**Unique and Other Set Logic**"""

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

print(np.unique(names))

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])

print(np.unique(ints))

print(sorted(set(names)))

values = np.array([6, 0, 0, 3, 2, 5, 6])

print(np.in1d(values, [2, 3, 6]))

"""**File Input and Output with Arrays**"""

arr29 = np.arange(10)

np.save('some_array', arr29)

np.load('some_array.npy')

"""**Linear Algebra**"""

# Dot การคูณเมตริกซ์

x = np.array([[1., 2., 3.], [4., 5., 6.]])
print(x)

print("--------------------------------------------------------------")

y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(y)

print("--------------------------------------------------------------")

print(x.dot(y))

print("--------------------------------------------------------------")

print(np.dot(x, y))