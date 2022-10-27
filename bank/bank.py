import re

def main():
    enter = input("Greeting: ")
    low = enter.lower()
    inpu = re.sub('[, -  ]', '', low)

    if inpu == "hello":
        print("$0")
    elif inpu == "hellonewman":
        print("$0")
    elif inpu == "hey":
        print("$20")
    elif inpu == "howyoudoing?":
        print("$20")
    else:
        print("$100")

main()