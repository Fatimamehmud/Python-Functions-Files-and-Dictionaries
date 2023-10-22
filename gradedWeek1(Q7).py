# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, 
#then add the word to a list called p_words.
textfile=open("school_prompt.txt", "r")
x=textfile.read()
print(x)
read_step=textfile.readlines()
p_words=[]
for i in read_step:
    val=i.split()
    for j in val: 
         if "p" in j:
            p_words.append(j)
print(p_words)
