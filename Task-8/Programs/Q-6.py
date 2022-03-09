import numpy as np
a = []
b = int(input("Size of array:"))

for i in range(b):
    print("Enter the" , i+1,"-st element for first array." , end = " ")
    a.append(int(input("Element : ")))
a = np.array(a)
print("The array is : " , a)
print("The data type of the array : " , a.dtype)
print("")
b = a.astype('float64')
print("The converted array is : " , b)
print("")
print("The convetred data type of the array : " , b.dtype)



