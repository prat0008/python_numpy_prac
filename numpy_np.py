"""import numpy as np
#1D array
x=np.array([1,2,3,4])
y=np.array([7,8,9,10])
a=np.dot(x,y)
print(a)
print(x)                   
print(x.shape)        #1D array shape

#2D array
climate_data=np.array([[73,67,43],
              [91,88,64],
              [87,134,58],
              [102,43,27],
              [69,96,70]])
print(climate_data)
print(climate_data.shape)  #2D array shape

#3D array
arr_3=np.array([
               [[11,12,13],
                [13,14,15]],

               [[15,16,17],
                [17,18,19]]])
print(arr_3)
print(arr_3.shape)           #3D array shape

#array elements need to be of same type and
#to check this we use dtype function (datatype)
#if there is one floating point nunber in an array then it will automatically
#converts to floating point if its all values are integer
print(x.dtype)
print(y.dtype)
print(climate_data.dtype)
print(arr_3.dtype)

arr=np.array([1,2,3,4,5,6,8.8])
print(arr)
print(arr.dtype)

weights=([0.3,0.2,0.5])
#matmul is used to do matrix multiplication
m=np.matmul(climate_data, weights)
print(m)
# @ character is also used to print matrixmultplication in numpy
print(climate_data @ weights)"""


#working with with the csv files

"""import numpy as np
import urllib.request
urllib.request.urlretrieve(
    'https://github.com/the-stranger-web/jovian_Data_Analyst/blob/main/italy-covid-daywise.csv',
    'italy.txt')

data=np.genfromtxt('italy.txt',delimiter=',',skip_header=1)
print(data)"""


"""import numpy as np
import urllib.request

# Use the raw content URL from GitHub instead of the HTML page
urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/the-stranger-web/jovian_Data_Analyst/main/italy-covid-daywise.csv',
    'italy-covid-daywise.txt')

data = np.genfromtxt('italy-covid-daywise.txt', delimiter=',', skip_header=1)
print(data)
print(data.shape)
"""
"""#arithemetic operations and broadcasting
import numpy as np
arr2=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,1,2,3]])
arr3=np.array([[11,12,13,14],
                [15,16,17,18],
                [19,11,12,13]])
#adding a scalar
print(20*"*")
print(arr2 + 3)
print(20*"*")
print(arr2 * 3)
print(20*"*")
print(arr3 - 3)
print(20*"*")
print(arr3 / 3)
print(20*"*")
print(arr2 % 3)

print("------------------------------------------------------------")

#element  wise operation
print(20*"*")
print(arr2 + arr3)
print(20*"*")
print(arr2 - arr3)
print(20*"*")
print(arr2 * a4rr3)
print(20*"*")
print(arr2 / arr3)
"""

"""import numpy as np
arr4=np.array([[1,2,3,4],
              [4,5,6,7],
              [8,9,10,11]])

arr5=np.array([12,13,14,15])
arr5_replication=np.array([[12,13,14,15],
                           [12,13,14,15],
                           [12,13,14,15]])
print("arr4 shape",arr4.shape)
print("arr5 shape",arr5.shape)
print(arr4 + arr5)
print(50*'*')
print("verification of result")
print(arr4 + arr5_replication)"""

"""#comparison operators in numpy 
import numpy as np
arr6=np.array([[1,2,3], [3,4,5]])
arr7=np.array([[2,2,3], [1,2,5]])

print(50*'*')
print("comparison oprtr")
print(arr6==arr7)
print(50*'*')
print("not equal oprtr")
print(arr6!=arr7)
print(50*'*')
print("grtr than equal to oprtr")
print(arr6>=arr7)  
print(50*'*')
print("less than oprtr")
print(arr6<arr7)"""


#array indexing and slicing
import numpy as np
"""arr=np.array([
    [[11,12,13,14],
     [13,14,15,19]],

    [[15,16,17,21],
     [63,92,36,18]],
    
    [[98,32,81,23],
     [17,18,19.5,23]]])"""

#array shape
#print(arr.shape)

#single element
#print(arr[1,1,2])
#print("explanation of above statement")
#print(arr[1])
#print(arr[1,1])
#print(arr[1,1,2])

#subarray using ranges
#print(arr[1:,0:1,:2])

#mixing indices and ranges
#print(arr[1:,1,3])
#print(arr[1:,1,:3])

#using fewer indices
#print(arr[1])
#print(arr[:2,1])

#other ways of creating numpy arrays
#all zeros
#print(np.zeros((3,2)))

#all ones
#a=np.ones([2,2,3])
#print(a)

#identity matrix
#print(np.eye(3))

#random vector
#print(np.random.rand(5))

#fixed value
#print(np.full([2, 3], 42))

#range with start,end and step
#print(np.arange(10,90,3))

#equally spaced numbers in a range
#print(np.linspace(3,27,9))