


def writeToList(a, path):
    try:
        f = open(path, 'r')
        for line in f:
            numbers = line.split()
            for i in numbers:
                try:
                    a.append(int(i))
                except ValueError:
                    continue
        f.close()
    except FileNotFoundError:
        print('File not found')


def maxE(a):
    try:
        maximum = a[0]
        for i in a:
            if i > maximum:
                maximum = i
        return maximum
    except IndexError:
        return None

def minE(a):
    try:
        minimum = a[0]
        for i in a:
            if i < minimum:
                minimum = i
        return minimum
    except IndexError:
        return None

def sumE(a):
    summ = 0
    for i in a:
        summ += i
    return summ

def prE(a):
    pr = 1
    for i in a:
        pr *= i
    return pr
