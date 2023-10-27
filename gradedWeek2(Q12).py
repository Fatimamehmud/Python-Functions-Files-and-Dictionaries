#Create the dictionary characters that shows each character from the string sally and its frequency. 
#Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
sally = "sally sells sea shells by the sea shore"
characters ={}

for achar in sally:
    if achar not in characters:
        characters[achar]=0
    characters[achar]=characters[achar]+1 

best_char = ''
highest_frequency = 0

for char, frequency in characters.items():
    if frequency > highest_frequency:
        best_char = char
        highest_frequency = frequency
