def swap_case(s):
    a = ""
    for i in s:
        if i.isupper() == True:
            a+=(i.lower())
        else:
            a+=(i.upper())
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
