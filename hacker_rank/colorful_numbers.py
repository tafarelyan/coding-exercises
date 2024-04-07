def isColorful(number):
    products = []
    number = str(number)

    for i in range(len(number)):
        product = 1
        for j in range(i + 1, len(number) + 1 if i != 0 else len(number)):
            product = product * int(number[j-1])

            if product in products:
                return False
            else:
                products.append(product)
    return True

if __name__ == '__main__':
    print(isColorful(3245))
    print(isColorful(326))
    print(isColorful(32656))