def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current

    return array

def main():
    array = [9, 3, 5, 1, 2, 4]
    array = insertion_sort(array)
    print(array)

if __name__ == '__main__':
    main()