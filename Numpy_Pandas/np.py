import numpy as np

lst = [1,2,3,4]
# print(type(lst))

arr = np.array(lst) # 1D array
# print(type(arr))


lst1 = [1,2,3,4]
lst2 = [1,2,3,4]
lst3 = [1,2,3,4]

# print(arr.shape) # return (rows,column)
arr1 = np.array([lst1,lst2,lst3]) # 2D array
# print(arr.shape)

# print(arr,arr1,sep='\n')

# print(arr[::-1])   #reverse from last

# print(arr1)

# dekho arr1[ yha row k lie  ,  col k lye ]

# print(arr1[:,3]) # print all column of 2D arr
  
# print(arr1[1:,1:3]) 

# print(arr1[1:,1:])

# print(arr1[1:,2:])

# print(arr1[:,2:].shape)

print(arr1[:,[0,3]])

# print(arr1[arr1 > 1])

# print(arr1.reshape(4,3)) # of same 3*4 to 4*3

# print(np.arange(1,30,3).reshape(5,2))
