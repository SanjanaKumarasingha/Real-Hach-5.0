def find_minimum_vertex_cover(P, Q, edges):
    graph = {i: [] for i in range(1, P + 1)}

    # Create an adjacency list representation of the graph
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    min_vertex_cover_size = 0

    for node in range(1, P + 1):
        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    min_vertex_cover_size += 2  # Include both nodes in the cover

    return min_vertex_cover_size

# Input
P, Q = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(Q)]

# Output
result = find_minimum_vertex_cover(P, Q, edges)
print(result)
