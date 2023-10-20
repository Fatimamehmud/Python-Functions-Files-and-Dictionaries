
#this is the content of the file school_prompt2.txt :
#Writing essays for school can be difficult but
#many students find that by researching their topic that they
#have more to say and are better informed. Here are the university
#we require many undergraduate students to take a first year writing requirement
#so that they can
#have a solid foundation for their writing skills. This comes
#in handy for many students.
#Different schools have different requirements, but everyone uses
#writing at some point in their academic career, be it essays, research papers,
#technical write ups, or scripts.


# Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

myfile=open("school_prompt2.txt","r")
line=myfile.read()
num_char=len(line)
print(num_char)
