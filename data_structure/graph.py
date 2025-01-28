from collections import deque, defaultdict
from typing import Dict


class Graph:
    """
    Graph represented using nodes and their adjacent nodes
    """

    class Node:
        __slots__ = ('val', 'neighbors')

        def __init__(self, val=None, neighbors=None):
            self.val = val
            self.neighbors = neighbors or []

    def bfs(self, root):
        if not root:
            return root
        queue = deque()
        new_node = self.Node(root.val, root.neighbors)
        node_map = {
            new_node.val: new_node
        }
        queue.append(new_node)
        while len(queue):
            n = queue.popleft()

            # processing of a node include - updating the neighbors
            # as we are updating the neighbors,
            # It does not make sense to handle the case of :root node's clone initialization in the while loop.
            neigbhors = []
            for node in n.neighbors:
                if node.val not in node_map:
                    node_map[node.val] = self.Node(node.val, node.neighbors)
                    queue.append(node_map[node.val])
                neigbhors.append(node_map[node.val])
            node_map[n.val].neighbors = neigbhors

        return new_node

    def dfs(self, root, node_map: Dict[int, Node] = dict):
        # check if a node is visited
        if root.val in node_map:
            return node_map[root.val]
        node_map[root.val] = self.Node(root.val, root.neighbors)

        new_neighbors = []
        # clone and iterate the neighbors of visited node.
        for n in node_map[root.val].neighbors:
            new_neighbors.append(self.dfs(n, node_map))
        node_map[root.val].neighbors = new_neighbors
        return node_map[root.val]

    def cloneGraph(self, node: 'Node') -> 'Node':
        # if not node:
        #     return node
        # node_map = {}
        # return self.dfs(node, node_map)
        return self.bfs(node)

    @classmethod
    def topological_sorting(cls, edges, node_no):
        """
        Implemented using BFS (Kahn's Algo)
        Returns the topological order. Raises Exception in case there is cycle.
        :param edges: list of "directed" edges in a graph (not necessary that all nodes in a graph are connected, ie. any edge to be present)
            Edges are 0 index based.
        :param node_no: Number of nodes
        :return: list of nodes in topological order
        """
        # prepare adjacency list and compute in-degree
        adj_graph = defaultdict(list)
        in_degree = [0] * node_no
        for edge in edges:
            adj_graph[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1

        queue = deque()
        leaves = [idx for idx, val in enumerate(in_degree) if val == 0]
        queue.extend(leaves)

        topo_ordering = []

        """
        Remove leaves nodes one by one (and update in degree along). Leaves have in-degree == 0.
        In case not all nodes processed - it contain cycle.
        There is no need for visited, as we track the visit by setting in-degree to 0. 
        And we add these node to queue whenever - we make then eligible (i.e no dependency for them) for processing
        """
        while queue:
            node = queue.popleft()
            topo_ordering.append(node)

            for to in adj_graph[node]:
                # reduce in degree due to node removal
                in_degree[to] -= 1
                # add those node to queue - which have become leaf
                if in_degree[to] == 0:
                    queue.append(to)

        if len(topo_ordering) < node_no:
            raise Exception('Graph contain cycle')
        return topo_ordering

    @classmethod
    def topological_sorting_dfs(cls, edges, node_no):
        """
        Implemented using DFS
        Returns the topological order
        :param edges: list of "directed" edges in a graph (not necessary that all nodes in a graph are connected, ie. any edge to be present)
            Edges are 0 index based.
        :param node_no: Number of nodes
        :return: list of nodes in topological order
        """
        # We can detect cycles using this - but we need to maintain a separate set of nodes which we have visited in the current path
        adj_graph = defaultdict(list)
        for edge in edges:
            adj_graph[edge[0]].append(edge[1])
        visited = [False] * node_no

        ans = []

        """
        We are inserting the nodes into the stack after the completion of the traversal, 
        we are making sure, there will be no one who appears afterward but may come before in the
        ordering as everyone during the traversal would have been inserted into the stack.
        """
        def dfs(n, visited):
            visited[n] = True
            for it in adj_graph[n]:
                if not visited[it]:
                    dfs(it, visited)
            ans.append(n)

        for node in range(node_no):
            if not visited[node]:
                dfs(node, visited)
        ans.reverse()
        return ans

# Graph.topological_sorting(edges=[[3,0],[3,1],[3,2],[3,4],[5,4]], node_no=6)
# Graph.topological_sorting_dfs(edges=[[3,0],[3,1],[3,2],[3,4],[5,4]], node_no=6)
