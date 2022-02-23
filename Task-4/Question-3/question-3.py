#Write a python program to make a 2-dimensional list that contains represents a table of records, for instance, student details like Roll no, Student Name, Marks; And complete the following 2 sub-tasks.
#i) Add some records in the list and print the list in tabular form.
#ii) From created list, extract and print second record/row that contains
import pandas as pd
element=[]
n=int(input("Enter number of students:"))
for s in range(0,n):
    print("Enter details of each students (Roll_number, Name, Marksobtained):")
    element.append([])
    for a in range(0,4):
        if a==0:
            Add_details = input("Enter Roll_number:")
        elif a==1:
            Add_details=input("Enter Name:")
        elif a==2:
            Add_details = input("Enter Marksobtained:")
        elif a==3:
            Add_details=" "
        element[s].append(Add_details)
print(element)
df = pd.DataFrame(element, columns=["Roll_number.", "Name", "Marksobtained",""])
df = df.set_index(["Roll No.", "Name","Marksobtained"])
print(df)
print("")
print("Second row is:")
print(df[1:2])
