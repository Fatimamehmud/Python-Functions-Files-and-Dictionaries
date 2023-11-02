# 2. Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(s1):
    acount=0
    for i in s1:
        acount=acount+1
    return acount

    
    
x=[]  
t=int(input("please enter the range:"))
for i in range(t):
    x.append(int(input("enter the number:")))
             
print(count(x)) 
            
