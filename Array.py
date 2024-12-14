#Array operations:

import array as arr
import numpy as np

a= arr.array('i',[1,3,5,6]) #Accessing element
ar= np.array([8,9,7]) #Accessing element
ar2= np.array([3,4,5]) #Accessing element

sub= a[1:9] #Slicing

a.append(8) # Appending an element

a.pop() #popping element

a.remove(6) # remove element

arr=a.index(3) # finding index value

a.insert(0,9) #insert element

a.extend([1,2,3]) # extend element

a.reverse() # reverse elements

a.count(5) # count elements

prod=np.dot(ar,ar2) #95; product od two arrays

ar3=ar2+5 #[8 9 7] ; Adding 5 to each element in array
su=np.sum(ar) #24
print(su) 

ad= ar+ar #[16 18 14]; Addition of two arrays

zer=np.zeros(7)#  [0. 0. 0. 0. 0. 0. 0.]
on=np.ones(3) # [1. 1. 1.]
ran=np.random.rand(2)
n=arr.reshape(1,5)



# arr=a.index(3)
# print(arr)
# print(ar)