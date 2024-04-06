def merge_sort(array):
    if len(array) == 1:
        return array

    divide = len(array) // 2
    left_array = merge_sort(array[:divide])
    right_array = merge_sort(array[divide:])

    return merge(left_array, right_array)

def merge(left_array, right_array):
    array = []
    i = 0
    j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array.append(left_array[i])
            i += 1
        else:
            array.append(right_array[j])
            j += 1

    while i < len(left_array):
        array.append(left_array[i])
        i += 1

    while j < len(right_array):
        array.append(right_array[j])
        j += 1

    return array

def main():
    array = [9, 3, 5, 1, 4, 2, 3]
    array = merge_sort(array)
    print(array)

if __name__ == '__main__':
    main()