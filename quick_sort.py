def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]

    left_array = [x for x in array if x < pivot]
    middle_array = [x for x in array if x == pivot]
    right_array = [x for x in array if x > pivot]

    return quick_sort(left_array) +  middle_array + quick_sort(right_array)

def main():
    array = [9, 3, 5, 1, 2, 4, 6, 7]
    array = quick_sort(array)
    print(array)

if __name__ == '__main__':
    main()