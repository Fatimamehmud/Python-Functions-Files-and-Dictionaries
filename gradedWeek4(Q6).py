# Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. 
# The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(a,b=True,dict1={2:3, 4:5, 6:8}):
    if b==True:
        for i in dict1.keys():
            if i ==a:
                return dict1[i]
    else:
        return b
      
# print(test(4)
# or
# print(test(4,False)) 

