def dfs(visited, graph, node):
    if node not in visited:
        print(node)

        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def main():
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': [],
    }

    visited = set()
    dfs(visited, graph, '5')

if __name__ == '__main__':
    main()