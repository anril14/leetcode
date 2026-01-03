graph = dict({
    'a': ['b', 'c'],
    'b': ['e'],
    'c': ['d', 'f'],
    'd': ['e'],
    'e': ['g'],
    'f': ['e'],
    'g': []
})


def bfs(graph, start):
    visited = set()
    visited.add(start)
    queue = [start]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node)
        print(queue)

        for i in graph[node]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
    return visited


if __name__ == '__main__':
    print(bfs(graph, 'a'))
