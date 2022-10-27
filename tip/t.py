L = [':)','B','C','D','E']
N = ['🙂','2','3','4','5']
n_strings = ['124','351'] # Don't use list as a variable name

while not all( x.isalpha() for x in n_strings): # keep going until all are alpha chars

    print ("Enter a letter")
    # Is there a number in List
    # If yes then do the following else print List

    # Ask for a letter from the user
    letter = input("Enter letter: ")

    # Confirm whether the letter is correct or not
    if letter in L:
    # Find the position of the letter in the list
        position = (L.index(letter));
    # Make a variable called number with value at the same position in the N list
        number = N[position];
    # Replace the numbers in the List with the letter entered
        n_strings = [item.replace(number, letter) for item in n_strings];
    # Print the list with the numbers replaced
        print (n_strings, "\n");
        print ("Please guess again. \n");
        letter = input("Enter a letter now: ")
    # repeat until the List only contains letters
    else:
        print ("That is not correct");
        print ("Please guess again. \n");
        letter = input("Enter a letter now: ")