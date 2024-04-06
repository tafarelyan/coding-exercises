from collections import deque

commands = """
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
"""
commands = [command.strip() for command in commands.strip().split('\n')]

queries = commands.pop(0)

queue = deque()
for command in commands:
    query = [int(x) for x in command.split()]
    if query[0] == 1:
        queue.append(query[1])
    elif query[0] == 2:
        queue.popleft()
    elif query[0] == 3:
        print(queue[0])