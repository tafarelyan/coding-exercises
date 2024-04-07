def insertionSort2(n, arr):
    for r in range(1, n):
        current = arr[r] 

        l = r - 1
        while l >= 0 and arr[l] > current:
            arr[l + 1] = arr[l] # swap right 
            arr[l] = current
            l -= 1

        arr[l + 1] = current

        print(arr)


if __name__ == "__main__":
    insertionSort2(6, [1, 4, 3, 5, 6, 2])