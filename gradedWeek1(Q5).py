# We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.
emotion="emotion_words.txt"
file_step=open(emotion,"r")
read_step=file_step.readlines()
num_words=0
for i in read_step:
    num_words=num_words+ len(i.split())     
print(num_words)
file_step.close
x=file_step.read()
print(x)
