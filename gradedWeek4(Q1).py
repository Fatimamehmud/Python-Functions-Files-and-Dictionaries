# Write a function called stop_at_four that iterates through a list of numbers. 
# Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.
def stop_at_four(list1):
    list2=[]
    dx=0
    if 4 not in list1:
        return list1
    
    while dx<len(list1):
        if list1[dx]!=4:
            list2.append(list1[dx])
        else:
            break
        dx=dx+1
    return list2 

y=input("enter the range:")
x=[]
for i in range(int(y)):
     t=input("enter the number:")
     x.append(int(t))
              
print(stop_at_four(x))
