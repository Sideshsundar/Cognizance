import numpy as np
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = b + 1
nums = np.arange(a,c)
print("Original array:")
print(nums)
p = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(p))
new_nums[::p+1] = nums
print("\nNew array:")
print(new_nums)