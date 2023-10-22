# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
textfile=open("school_prompt.txt", "r")
x=textfile.read()
print(x)
read_step=textfile.readlines()
three=[]
for i in read_step:
    val=i.split()
    three.append(val[2])
print(three)
