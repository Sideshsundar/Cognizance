#Question-5
#Print the following pattern.
a = int(input("Enter a number:"))
b = (2*a)-2
for i in range(0,a):
    for j in range(0,b):
        print(end=" ")
    b = b - 1
    for j in range(0 , i + 1):
        print("* ", end="")
    print("")
