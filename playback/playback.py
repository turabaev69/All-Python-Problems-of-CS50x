text = input("please write something:")#getting input from a user

text2 ='' #creating a variable for "space"

for i in range(len(text)): #looping through text
    if(text[i] ==" "): #checks whether ' ' is in text or not
        text2 = text2 + '...'
    else:
        text2 = text2 + text[i]

print("This is the output:", text2) #print the output
