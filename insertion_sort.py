def insertion_sort(array):
    for r in range(1, len(array)):
        current = array[r]
        l = r - 1
        while l >= 0 and array[l] > current:
            array[l + 1] = array[l]
            l -= 1

        array[l + 1] = current

    return array

def main():
    array = [9, 3, 5, 1, 2, 4]
    array = insertion_sort(array)
    print(array)

if __name__ == '__main__':
    main()