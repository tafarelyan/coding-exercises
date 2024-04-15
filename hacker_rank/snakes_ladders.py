from pprint import pprint

def quickestWayUp(ladders, snakes):
    ladders = {
        start: end
        for start, end in ladders
    } 

    snakes = {
        start: end
        for start, end in snakes
    } 

    position = 1
    visited = {
        1: 0
    }
    queue = [1]

    while queue:
        position = queue.pop(0)

        if visited.get(100):
            return visited[100]
        
        for position_ in range(position + 6, position, -1):
            if ladders.get(position_):
                position_ = ladders[position_]
            elif snakes.get(position_):
                position_ = snakes[position_]

            if position_ not in visited:
                visited[position_] = visited[position] + 1
                queue.append(position_)
            elif visited[position_] > visited[position] + 1:
                visited[position_] = visited[position] + 1
    return -1
        
if __name__ == '__main__':
    print(quickestWayUp(
        [[32,62],[42,68],[12,98]],
        [[95,13],[97,25],[93,37],[79,27],[75,19],[49,47],[67,17]]
    ))
