#. Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5.
#mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.

def addit(a):
   add =int(a)+5
   return add


def mult(a):
    k=addit(a)
    y=int(a)*k
    return y

x=mult(input("entern the number:"))
print(x)
