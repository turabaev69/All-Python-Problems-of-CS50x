import re

def main():
    inputt = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ").lower()

    inpu = re.sub('[- -  ]', '', inputt)
    if inpu == "42":
        print("Yes")
    elif inpu == "fortytwo":
        print("Yes")
    else:
        print("No")
main()