def rotLeft(a, d):
    for _ in range(d):
        element = a.pop(0)
        a.append(element)

    return a

if __name__ == '__main__':
    print(rotLeft(5, 4))