def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'A': set(['D', 'C','B']),
         'B': set(['A']),
         'C': set(['B']),
         'D': set(['C'])
         }

dfs(graph, 'D')
