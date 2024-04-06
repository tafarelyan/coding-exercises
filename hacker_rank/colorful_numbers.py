from functools import reduce

def isColorful(number):
    products = []
    number = str(number)
    for i in range(1, len(number)):
        for j in range(len(number) + 1 - i):
            product = reduce(lambda a, b: a * b, [int(x) for x in number[j:i+j]])
            if product in products:
                return False
            else:
                products.append(product)
    
    return True

if __name__ == '__main__':
    print(isColorful(3245))
    print(isColorful(326))
    print(isColorful(32656))
