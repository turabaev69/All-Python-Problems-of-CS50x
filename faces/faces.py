def main():
    enter = input("enter: ") #ask the user an input
    if ":)" in enter: # check whether
        d = enter.replace(":)", '🙂') #convert :) to 🙂 by replace
    elif ":(" in enter:
        d = enter.replace(":(", '🙁') #convert :( to 🙁 by replace

    print(d) #printing the output
main()




