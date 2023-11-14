# Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) 
#If you want to make this even more of a challenge, do this without slicing
def beginning(a):
    x=0
    k=[]
    while x<len(a):
        if a[x]!="bye" and len(k)<10:
            k.append(a[x])
           
        else:
            break
           
        x=x+1
    return k

t=['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']

              
print(beginning(t))
