import heapq
from collections import deque


# BFS - unweighted_shortest_path
# We need to keep visited to avoid reprocessing. This is possible even if there is no cycle
# Unless we have a graph with at-max 1 in-degree and 1 out degree
def unweighted_shortest_path(graph, src, dest):
    queue = deque([(src, 0)])
    visited = set()
    while queue:
        node, dist = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == dest:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                queue.append((nei, dist + 1))

    return -1


unweighted_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(unweighted_shortest_path(unweighted_graph, 'A', 'F'))  # Output: 2


# Dijkstra - Shortest Path with non-negative weight
# - We use priority queue to pick the lowest current distance
# - Edge relaxation for each node - update shortest known distance to each neighbor
# Here the distance check is used to avoid redundant processing, if the stored distance from src to nei is
# smaller than current distance - we can form, that mean we have visited this nei from a more optimal path

def dijkstra(graph, src):
    # Distances store the lowest distance to the node from :src
    distances = {node: float('inf') for node in graph}
    distances[src] = 0
    pq = [(0, src)]
    while pq:
        dist, curr = heapq.heappop(pq)

        if dist > distances[curr]:
            # if we already have a smaller path, no need to visit again
            continue

        for nei, weight in graph[curr]:
            distance = dist + weight
            # we only paths from nei only when we dont have a path with lesser distance
            # That means the presence of a lesser distance mean that i have already visited the nei with a small distance
            # And any distance to other nodes from nei will be smaller in the previous run (when we set the lower cost path)
            # Although it is not necessary that, new paths
            if distance < distances[nei]:
                distances[nei] = distance
                heapq.heappush(pq, (distance, nei))

    return distances


positive_weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print(dijkstra(positive_weighted_graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}


# Bellman Ford - Shortest path in graphs with negative weights
# It handle both negative and positive cycles
# Relaxation of edge means - updating a path to a another smaller path (distances[nei] > distances[node] + wt)

def bellman_ford(graph, src):
    distances = {node: float('inf') for node in graph}
    distances[src] = 0

    # As the longest path possible with a v vertex is v - 1 edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for nei, wt in graph[node]:
                if distances[nei] > distances[node] + wt:
                    distances[nei] = distances[node] + wt

    for node in graph:
        for nei, wt in graph[node]:
            if distances[nei] > distances[node] + wt:
                raise Exception('Negative cycle present')

    return distances


negative_weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', -3), ('D', 2)],
    'C': [],
    'D': [('B', 1)]
}
print(bellman_ford(negative_weighted_graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': -2, 'D': 3}

# Floyd Warshall - All-pairs shortest path in graphs without negative cycles

def floyd_warshall(graph):
    nodes = list(graph.keys())
    distances = {node: {nei: float('inf') for nei in nodes} for node in nodes}

    for node in nodes:
        distances[node][node] = 0
        for nei, wt in graph[node]:
            distances[node][nei] = wt

    for k in nodes:
        for i in nodes:
            for j in nodes:
                distances[i][j] = min(distances[i][k] + distances[k][j], distances[i][j])

    return distances

graph = {
    'A': [('B', 3), ('C', 8)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print(floyd_warshall(graph))

# Topological sorting + relaxation - Shortest path in a Directed Acyclic Graph (DAG)

def topological_sort(graph):
    # assuming graph has all the nodes in it, even if there is no edge from it.
    visited = set()
    ans = []

    def dfs(n):
        visited.add(n)
        for nei, _ in graph[n]:
            if nei not in visited:
                dfs(nei)
        # We add the node to the ans - once we have processed all its dependencies
        # i.e. all the nodes which can be traversed from this node `n`
        ans.append(n)

    for node in graph:
        # visited is needed to prevent redundant processing, even when there is no cycle - due to needed this forloop for
        # disconnected graph
        if node not in visited:
            dfs(node)

    ans.reverse()
    return ans

def dag_shortest_path(graph, start):
    # In processing nodes in order of this list - mean that for each node there are no remaining dependencies we need to process this node
    order = topological_sort(graph)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    for node in order:
        for nei, wt in graph[node]:
            if distances[nei] > distances[node] + wt:
                distances[nei] = distances[node] + wt

    return distances

graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('C', 3), ('D', 6)],
    'C': [('D', 4)],
    'D': []
}
print(dag_shortest_path(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 2, 'D': 6}