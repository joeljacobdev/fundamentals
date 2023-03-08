from collections import deque
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

    def dfs(self, root, node_map: Dict['Node'] = dict):
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
