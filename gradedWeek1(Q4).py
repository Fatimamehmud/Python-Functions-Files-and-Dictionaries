#this is the content of file :
# Sad upset blue down melancholy somber bitter troubled
#Angry mad enraged irate irritable wrathful outraged infuriated
#Happy cheerful content elated joyous delighted lively glad
#Confused disoriented puzzled perplexed dazed befuddled
#Excited eager thrilled delighted
#Scared afraid fearful panicked terrified petrified startled
#Nervous anxious jittery jumpy tense uneasy apprehensive
# Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
myfile=open("emotion_words.txt ","r")
num_lines=0
for line in myfile.readlines():
    num_lines=num_lines+1
print(num_lines)
