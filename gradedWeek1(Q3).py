#this is content of the file:
#Sad upset blue down melancholy somber bitter troubled
#Angry mad enraged irate irritable wrathful outraged infuriated
#Happy cheerful content elated joyous delighted lively glad
#Confused disoriented puzzled perplexed dazed befuddled
#Excited eager thrilled delighted
#Scared afraid fearful panicked terrified petrified startled
#Nervous anxious jittery jumpy tense uneasy apprehensive

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

myfile=open("emotion_words2.txt","r")
first_forty =myfile.read(40)
print(first_forty)
