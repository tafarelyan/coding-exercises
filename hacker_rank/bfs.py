def bfs(n, m, edges, s):
    graph = {}
    for i in range(n):
        graph[i + 1] = []

    for edge in edges:
        graph[edge[0]].append(edge[1])

    levels = {
        i+1: -1
        for i in range(n)
    }

    levels[s] = 0
    queue = [s]

    while queue:
        head = queue.pop()
        for neighbor in graph[head]:
            if levels[neighbor] == -1:
                queue.append(neighbor)
                levels[neighbor] = 1 + levels[head]
            elif levels[neighbor] > levels[head] + 1:
                levels[neighbor] = 1 + levels[head]

    del levels[s]
    return [x * 6 if x != -1 else -1 for x in levels.values()]

if __name__ == '__main__':
    print(bfs(4, 2, [[1,2], [1,3]], 1))
    print(bfs(3, 1, [[2,3]], 2))
    print(bfs(5, 3, [[1,2],[1,3],[3,4]], 1))
    print(bfs(7, 6, [[2,3],[2,4],[3,5],[3,6],[4,6],[6,7]], 2))