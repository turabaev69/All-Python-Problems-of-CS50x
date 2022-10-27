# def main(enter):




def change_case(str):
    res = [str[0]]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
        else:
            res.append(c)

    return ''.join(res)

# Driver code
str = "GeeksForGeeks baaa"
print(change_case(str))