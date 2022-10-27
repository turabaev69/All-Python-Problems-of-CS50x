import re

def main():
    name = input("camelCase: ")
    for i in range(len(name)):
        if "ABCDEFGHIJKLMNOPQRSTUVWXYZ" in name:
            new =  i.append(' _')
            print(new)


main()
#name = 'CamelCaseName'


# camelCase = input("camelCase: ")


# for i in range(len(camelCase)):
#     print(camelCase[1::])