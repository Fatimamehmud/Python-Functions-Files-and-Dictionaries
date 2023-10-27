# Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, 
#find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
characters={}

for achar in sally:
    if achar not in characters:
        characters[achar]=0
    characters[achar]=characters[achar]+1

worst_char = ''
lowest_frequency = 1000

for char, frequency in characters.items():
    if frequency <lowest_frequency:
        worst_char = char
        lowest_frequency = frequency

print(characters)
print( worst_char)
