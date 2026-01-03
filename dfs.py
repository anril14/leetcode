graph = dict({
    'a': ['b', 'c'],
    'b': ['e'],
    'c': ['d', 'f'],
    'd': ['e'],
    'e': ['g'],
    'f': ['e'],
    'g': []
})


def dfs(graph, start):
    visited = set()
    visited.add(start)
    stack = [start]

    while len(stack) > 0:
        node = stack.pop()
        print(node)
        print(stack)

        for i in graph[node]:
            if i not in visited:
                stack.append(i)
                visited.add(i)

    return visited


if __name__ == '__main__':
    print(dfs(graph, 'a'))
