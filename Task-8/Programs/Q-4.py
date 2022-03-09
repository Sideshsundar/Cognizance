import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering','chennai' , 'campus'])
print("The series before captialising the series : ")
for i in ser:
    print(i , end = " ")
print("")
print("")
print("The series after captialising the series : ")
for j in ser:
    a = j
    b = a.capitalize()
    print(b , end = " ")
