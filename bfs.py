def bfs(visited, graph, initial_node):
    queue = []

    visited.append(initial_node)
    queue.append(initial_node)

    while queue:
        m = queue.pop(0)
        print(m, end = " ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

def main():
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': [],
    }

    visited = []
    bfs(visited, graph, '5')

if __name__ == '__main__':
    main()