# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(a):
    x=0
    y=[]

    while x<len(a):
        if a[x]!="STOP":
            y.append(a[x])
        else:
            break
           
        x=x+1
    return y
k=input("enter the range:")
t=[]
for i in range(int(k)):
    m=input("enter the number:")
    z=m.upper()
    t.append((z))
              
print(sublist(t))
