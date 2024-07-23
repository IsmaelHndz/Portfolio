def lucky_number(n):
    x = list(map(int, str(n)))
    if len(x) % 2 == 0:
        a = 0
        b = 0
        for i in range (0, int(len(x)/2)):
            a = x[i] + a
        for j in range (0, int(len(x)/2)):
            b = x[j + int(len(x)/2)] + b

        if a == b:
            print("This is a lucky number!")
            return True
        else:
            return False
    else:
        a = 0
        b = 0
        for i in range (0, int(len(x)/2)):
            a = x[i] + a
        for j in range (0, int(len(x)/2)):
            b = x[j + int(len(x)/2)+1] + b

        if a == b:
            print("This is a lucky number!")
            return True
        else:
            return False
    

if  __name__ == '__main__':
    print(lucky_number(12303))