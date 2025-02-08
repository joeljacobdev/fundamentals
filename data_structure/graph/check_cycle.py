from collections import defaultdict, deque

# Directed graph
directed_graph = {
    'A': [('B', 1)],
    'B': [('C', 3)],
    'C': [('D', 4)],
    'D': [('A', 3)]
}

directed_graph_no_cycle = {
    'A': [('B', 1)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 4)],
    'D': []
}


# We require rec_stack - so see if the node is visited in the current path again
# Visited just tell us that we have visited the node - it could be in the same path or in a different path
# But to know if cycle occurs - we want to only know if visited in the same path
# we can visualize rec_stack as subset of visited.
# Notes - weight does not matter in the cycle detected

def _dfs_check_cycle_in_directed_iterative(n, graph, visited, rec_stack):
    stack = [(n, 0)]
    visited[n] = True
    rec_stack.add(n)

    while stack:
        # idx is used to emulate current child we are processing for this "curr" node
        curr, idx = stack.pop()
        if idx < len(graph[curr]):
            nei, _ = graph[curr][idx]
            # we re-add if there are more neigbhors to visit (here we add it an extra 1 more time)
            stack.append((curr, idx + 1))

            if nei in rec_stack:
                return True
            if nei not in visited:
                visited[nei] = True
                rec_stack.add(nei)
                stack.append((nei, 0))
        else:
            rec_stack.remove(curr)


def _dfs_check_cycle_in_directed_recursive(n, graph, visited, rec_stack):
    if n in rec_stack:
        return True
    if visited[n]:
        return False

    visited[n] = True
    rec_stack.add(n)
    for nei, _ in graph[n]:
        if _dfs_check_cycle_in_directed_recursive(nei, graph, visited, rec_stack):
            return True
    rec_stack.remove(n)
    return False


def dfs_check_cycle_in_directed(graph):
    visited = defaultdict(bool)
    rec_stack = set()

    for n in graph:
        if n not in visited and _dfs_check_cycle_in_directed_recursive(n, graph, visited, rec_stack):
            return True
    return False


print("Directed Graph with cycle: DFS (rec stack): ", dfs_check_cycle_in_directed(graph=directed_graph))
print("Directed Graph without cycle: DFS (rec stack): ", dfs_check_cycle_in_directed(graph=directed_graph_no_cycle))


# This is detecting cycle using DFS version of topological sort.
def topo_sort_with_cycle_detection(graph) -> (bool, list):
    visited = set()
    # Nodes currently being explored (ie we can get current path if we have used a list)
    recStack = set()
    ans = []

    def dfs(n):
        # This means that in a given path we are visiting the same node again - which means cycle
        if n in recStack:
            return True
        # it is fine to re-visit to here from a different node - ie. reaching a same node from a different path
        if n in visited:
            return False

        # Mark node as being explored (nodes paths are explored with node n in path
        recStack.add(n)

        for nei, _ in graph[n]:  # Explore neighbors
            if dfs(nei):
                return True  # If cycle found in DFS, propagate failure

        # Now that we have explored all the paths leading from node n - we can remove it.
        recStack.remove(n)
        # We only mark a node as visited - once we have explored all the possibilities (in a topo sort)
        # rec_stack will help us unhandle loop due to cycle
        visited.add(n)
        ans.append(n)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True, []  # Cycle detected

    # We reverse as the nodes - without dependency are added first in ans array during recursion.
    # Nodes without dependency are added in lower depth of the recursion call stack
    ans.reverse()
    return False, ans


print("Directed Graph with cycle: Topo sort (DFS): ", topo_sort_with_cycle_detection(graph=directed_graph)[0])
print("Directed Graph without cycle: Topo sort (DFS): ",
      topo_sort_with_cycle_detection(graph=directed_graph_no_cycle)[0])

# Undirected graph
undirected_graph = {
    'A': [('B', 1)],
    'B': [('C', 3)],
    'C': [('D', 4)],
    'D': [('A', 3)]
}

undirected_graph_no_cycle = {
    'A': [('B', 1)],
    'B': [('C', 3)],
    'C': [('D', 4)],
    'D': []
}


# Union find - intuition if we can connect both nodes of edge to same component - it means there is a cycle
# Rank is an optimization to keep the tree shallow, reducing the depth.
# It ensures that find(x) remains efficient (almost O(1)).
# Path compression + union by rank = super fast disjoint sets.

class UnionFind:
    def __init__(self):
        # For a node which is not connected to anything - it is the parent for it
        self.parent = {}
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        # Doing path compression - it might seem like a lot of redundant work being done due to this
        # But If the paths are already compressed - the next call of find will directly point to the root parent node
        # in this connected graph, which will be x == self.parent[x]
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        # if not already connected
        if xr != yr:
            rank_xr = self.rank[xr]
            rank_yr = self.rank[yr]
            # attach smaller tree under larger tree
            # Although once the path compression has happened the tree with get shorted to 1 height - as all the nodes will point to parent
            if rank_xr > rank_yr:
                self.parent[yr] = xr
            elif rank_yr > rank_xr:
                self.parent[xr] = yr
            else:
                self.parent[xr] = yr
                self.rank[xr] += 1

    def has_cycle(self, x, y):
        return self.find(x) == self.find(y)


def check_cycle_union_find(graph):
    uf = UnionFind()
    for src in graph:
        for dest, _ in graph[src]:
            # One issue here is that we are processing both the direction of same edge (due to being represented as directed adj list)
            if uf.has_cycle(src, dest):
                return True
            uf.union(src, dest)
    return False


print("Undirected Graph with cycle: Union Find: ", check_cycle_union_find(graph=undirected_graph))
print("Undirected Graph without cycle: Union Find: ", check_cycle_union_find(graph=undirected_graph_no_cycle))

undirected_graph_double_edges = {
    'A': [('B', 1), ('D', 3)],
    'B': [('C', 3), ('A', 1)],
    'C': [('D', 4), ('B', 3)],
    'D': [('A', 3), ('C', 4)]
}

undirected_graph_double_edges_no_cycle = {
    'A': [('B', 1)],
    'B': [('C', 3), ('A', 1)],
    'C': [('D', 4), ('B', 3)],
    'D': [('C', 4)]
}


# Every undirected edge is present in both directions.
# What is the intuition that rec_stack was not needed here?
# - Cycle detection is simpler in undirected graph - as we can visit in both direction
# - If we can visit nei excluding the case when the parent is nei of n due to bidirectional edge - it has a cycle
def _dfs_parent_helper(n, parent, visited, graph):
    visited.add(n)
    for nei, _ in graph[n]:
        # parent == nei need to skip the back edge due to undirected. So if we have already visited and getting a nei which is not parent
        # Then there is cycle
        # path is parent <-> n <-> nei
        if nei in visited and nei != parent:
            return True
        if nei not in visited:
            if _dfs_parent_helper(nei, n, visited, graph):
                return True
    return False


def check_cycle_with_dfs_parent_undirected_graph(graph):
    visited = set()
    for n in graph:
        if n not in visited and _dfs_parent_helper(n, None, visited, graph):
            return True
    return False


print("Undirected graph with cycle: DFS parent ",
      check_cycle_with_dfs_parent_undirected_graph(undirected_graph_double_edges))
print("Undirected graph without cycle: DFS parent",
      check_cycle_with_dfs_parent_undirected_graph(undirected_graph_double_edges_no_cycle))


def _bfs_undirected_cycle_helper(n, graph, visited):
    q = deque([n])
    while q:
        curr = q.popleft()
        if curr in visited:
            return True
        visited.add(n)
        for nei, _ in graph[curr]:
            q.append(nei)


def check_cycle_with_bfs_undirected_graph(graph):
    visited = set()
    for n in graph:
        if n not in visited and _bfs_undirected_cycle_helper(n, graph, visited):
            return True
    return False


print("Undirected graph with cycle: BFS ", check_cycle_with_bfs_undirected_graph(undirected_graph))
print("Undirected graph without cycle: BFS ", check_cycle_with_bfs_undirected_graph(undirected_graph_no_cycle))
