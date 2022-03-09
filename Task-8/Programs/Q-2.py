import numpy as np
array1 = []
array = []
b = int(input("Size of array:"))

for i in range(b):
    print("Enter the" , i+1,"-st element for first array." , end = " ")
    array1.append(int(input("Element : ")))
array1 = np.array(array1)
print("The first array is : ")
print(np.floor(array1))
for i in range(b):
    print("Enter the" , i+1,"-st element second array." , end = " ")
    array.append(int(input("Element : ")))
array = np.array(array)
print("The second array is : ")
print(np.floor(array))
c = np.allclose(array1, array)
if (c == True):
    print("Both the arrays are equal.")
    print("Therefore : ", c)
else:
    print("Both the arrays are not equal.")
    print("Therefore : ", c)