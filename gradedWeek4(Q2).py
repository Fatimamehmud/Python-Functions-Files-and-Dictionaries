#Define a function called multiply.
#It should have one required parameter, a string.
#It should also have one optional parameter, an integer, named mult_int, with a default value of 10.
#The function should return the string multiplied by the integer. 
#(i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)
def multiply(a,mult_int=10):
    return a*mult_int

print(multiply("hi",3))
