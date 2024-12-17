#Array operations:

import array as arr
import numpy as np

a= arr.array('i',[1,3,5,6]) #Accessing element
ar= np.array([8,9,7]) #Accessing element
ar2= np.array([3,4,5]) #Accessing element
ar3 = [1,7,9,5]

sub= a[1:9] #Slicing

a.append(8) # Appending an element
ar=np.append(ar,[1,3])

a.pop() #popping element

a.remove(6) # remove element
ar=np.delete(ar,2) #Removes the element at index 2
ar=ar[ar !=3] #Removes all occurrences of 3

arr=a.index(3) # finding index value

a.insert(0,9) #insert element
np.where(ar == 3) #return the indices where the condition is True

a.extend([1,2,3]) # extend element

a.reverse() # reverse elements

a.count(5) # count elements

arr.sort() # Sorts in ascending order
arr.sort(reverse=True) #sorts in descending order
ar =np.sort(ar) #sorts in ascending order
ar = np.sort(ar)[::-1] # sorts in descending order

prod=np.dot(ar,ar2) #95; product od two arrays

ne_copy=ar.copy() # copy array

ar3=ar2+5 #[8 9 7] ; Adding 5 to each element in array
su=np.sum(ar) #24
print(su) 

ad= ar+ar #[16 18 14]; Addition of two arrays

zer=np.zeros(7)#  [0. 0. 0. 0. 0. 0. 0.]
on=np.ones(3) # [1. 1. 1.]

ran=np.random.rand(2) 

n=arr.reshape(1,5) # converts to 2*3 matrix

ar.clear() #clear the entire array

print(f"a\n ar\n ar2\n ar3\n")