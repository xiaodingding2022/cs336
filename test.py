import torch
import numpy as np


##x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)  
##y = x + 2  
##z = x @ y
##
##
##tensor_1d = torch.rand(1)
##tensor_2d = torch.rand(2,3)
##tensor_3d = torch.rand(2,3,4)

# print(tensor_1d, " - ", tensor_2d)

# arr = np.zeros((2, 3, 7),dtype=int)
##arr = np.random.rand(3,7)
##
##print(arr)
#batchs, rows, cols = arr.shape

##stride = 2
##window = 3
##idx = 0
##while idx + window - 1 < 7 :
##  print(arr[0:3,idx:idx+window])
##  idx += stride

a = np.array([[
    [1, 2, 3],
], [[8,9,10]]])

print(a.shape)
print(a.T.shape)
##b = np.array([[7, 8], [10, 11]])
##
### Sum along axis 1 (sum of rows within each slice)
##sum_axis_1 = np.tensordot(a,b,axes=(1))
##print("Sum along axis 1:\n", sum_axis_1)
##
### Sum along axis 2 (sum of columns within each slice)
##sum_axis_2 = np.tensordot(a,b,axes=(2))
##print("Sum along axis 2:\n", sum_axis_2)

##a = np.array([
##  [1,2,3],
##  [4,5,6]
##])
##
##b = np.array([
##  [0,2,3],
##  [1,5,6]
##])
##
##print(np.tensordot(a,b,0))
