#this is count of file travel_plans2.txt:
#This summer I will be travelling.
#I will go to...
#Italy: Rome
#Greece: Athens
#England: London, Manchester
#France: Paris, Nice, Lyon
#Spain: Madrid, Barcelona, Granada
#Austria: Vienna
#I will probably not even want to come back!
#However, I wonder how I will get by with all the different languages.
#I only know English!

# Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
myfile=open("travel_plans2.txt","r")
line=myfile.readlines()
num_lines=len(line)
print(num_lines)
