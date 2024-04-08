import heapq

if __name__ == '__main__':
    commands = [
        '1 4',
        '1 9',
        '3',
        '2 4',
        '3'
    ]

    heap = []
    for command in commands:
        query = [int(x) for x in command.split()]

        if query[0] == 1:
            heapq.heappush(heap, query[1])
        elif query[0] == 2:
            heap.remove(query[1])
        elif query[0] == 3:
            print(heap[0])

        print(heap)