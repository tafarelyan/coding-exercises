def quickSort(ar):
    if len(ar) <= 1:
        return ar

    pivot = ar[0]

    left = [x for x in ar if x < pivot]
    middle = [x for x in ar if x == pivot]
    right = [x for x in ar if x > pivot]

    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    print(quickSort([5, 8, 1, 3, 7, 9, 2]))