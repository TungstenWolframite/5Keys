a = ["a", "b", "c", "d", "e"]
b = ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
c = ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]
d = ["z"]
e = [" "]

def keys(x):
    if len(str(x)) == 1:
        return a[x-1]
    elif len(str(x)) == 2:
        if x < 20:
            return b[x-12]
        elif x > 20 and x < 30:
            return b[x-19]
        elif x > 30 and x < 40:
            return b[x-37]
        else:
            return b[x-36]
    elif len(str(x)) == 3:
        if x < 130:
            return c[x-123]
        elif x > 130 and x < 140:
            return c[x-131]
        elif x == 145:
            return c[x-140]
        elif x > 200 and x < 245:
            return c[x -228]
        elif x == 245:
            return c[8]
        elif x == 345:
            return c[9]
    elif len(str(x)) == 4:
        return d[0]
    else:
        return e[0]

def res(x):
    x = x.replace("f", "5")
    x = x.replace("h", "1")
    x = x.replace("7","2")
    x = x.replace("8","3")
    x = x.replace("9","4")
    x = x.replace("0","5")
    return x

def cap(x):
    if x[0] == "`" or x[0] == "6":
        return str(keys(int(x[1:]))).title()
    else:
        return keys(int(x))

def tran(x):
    z = 0
    trans = []
    final = ""
    for i in range(0, len(x)):
        if x[i] == " ":
            trans.append(x[z:i])
            z = i+1
    trans.append(x[z:])
    for i in trans:
        final += str(cap(i))
    return final

while True:
    x = input("What's your message?: ")
    x = res(x)
    print(tran(x))
