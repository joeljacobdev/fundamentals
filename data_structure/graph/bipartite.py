from collections import deque
from typing import List


# check for bipartite by checking if we have adjacent nodes in same group
# While traversing a graph - we reach a node again with bfs - if there is a cycle.
# We can also conclude that if there is a odd length cycle - it is not bipartite graph
# Instead of checking for cycle length - we can just do graph coloring.
# (For intuition check graph coloring example in [[bipartite graph]] notes)
def is_bipartite(graph: List[List[int]]) -> bool:
    visited = [0] * len(graph)

    def bfs(n):
        q = deque()
        q.append(n)
        visited[n] = -1
        while q:
            curr = q.popleft()
            for nei in graph[curr]:
                if visited[nei] == 0:
                    visited[nei] = visited[curr] * -1
                    q.append(nei)
                elif visited[nei] == visited[curr]:
                    # if visited is in same group as nei - then it is not bipartite
                    # This is also an odd length cycle.
                    return False

        return True

    for i in range(len(graph)):
        # doing this as this can be a disconnected graph
        if visited[i] == 0 and not bfs(i):
            return False

    return True
