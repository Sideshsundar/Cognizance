#Question-4
#Write a program to check if the given number is a palindrome number.
s=int(input("Enter a number:"))
a=str(s)
if(a==a[::-1]):
    print("The number", s ,"is a pallidrone")
else:
    print("The number", s ,"is not a pallidrone")
