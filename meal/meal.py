def main():
    enter = input("enter: ")
    new = enter.split(":")
    hour = int(new[0])
    min = int(new[1])

    if hour == 7 and min >= 0:
        print("breakfast time")
    elif hour == 18 and min >= 0:
        print("dinner time")
    elif hour == 12 or 13 and min >= 0:
        print("lunch time")

main()