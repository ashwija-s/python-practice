def dfs(graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            for i in range(len(graph[node])-1,-1,-1):
                if graph[node][i] == 1:
                    stack.append(i)
    return visited

graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(dfs(graph, 1))  # [1, 0, 2, 3]