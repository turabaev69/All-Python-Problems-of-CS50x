def ad(x, y):
    return x + y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def min(x, y):
    return x - y


def main():
    enter = input("enter: ")

    new = enter.split(" ")
    nm1 = int(new[0])
    p = new[1]
    nm2 = int(new[2])
    if p  == "+":
        print(float(ad(nm1, nm2)))

    if p  == "*":
        print(float(mul(nm1, nm2)))

    if p  == "/":
        print(float(div(nm1, nm2)))

    if p  == "-":
        print(float(min(nm1, nm2)))

main()