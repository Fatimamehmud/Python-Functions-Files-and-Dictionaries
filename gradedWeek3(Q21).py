#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(x):
    acumm=0
    for i in x:
        acumm= acumm+i
    return  acumm


x=input("the number you want add:")
lists=[]
for i in range(int(x)):
    x=input("enter the number:")
    lists.append(int(x))
print(accum(lists))
