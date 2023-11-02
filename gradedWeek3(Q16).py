# Write a function named total that takes a list of integers as input,
# and returns the total value of all those integers added together.
def total(s1):
    y=0
    for i in s1:
        y=i+y
    return y
      
x=[]  
t=int(input("please enter the range:"))
for i in range(t):
    x.append(int(input("enter the number:")))
             
print(total(x))
