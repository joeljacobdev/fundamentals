class Tree:
    class Node:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    @staticmethod
    def __ino_idx_to_idx(pre_post, inorder):
        """
        :param pre_post: pre/post order array
        :param inorder: inorder array of same tree as pre/post tree
        :return: array of inorder idx to pre_post order index
        """
        val_to_prepost_idx_map = {val: idx for idx, val in enumerate(pre_post)}
        dp = [0] * len(inorder)
        for idx, val in enumerate(inorder):
            dp[val_to_prepost_idx_map[val]] = idx
        return dp

    @classmethod
    def construct_tree_ino_preorder(cls, inorder, preorder):
        # we use preorder to identify the placement of root in subtree, while using inorder to decide the subtree
        mapping = cls.__ino_idx_to_idx(pre_post=preorder, inorder=inorder)
        n = len(inorder)

        def helper(start, end):
            if start == end:
                return cls.Node(inorder[start])
            if end < start or start > end:
                return None

            node_idx = n
            pre_idx = n
            """
                pre order will have root at left. 
                So the leftmost in the inorder range given is root node of subtree defined by [start, end]
            """
            for in_idx in range(start, end + 1):
                if pre_idx > mapping[in_idx]:
                    node_idx = in_idx
                    pre_idx = mapping[in_idx]

            node = cls.Node(inorder[node_idx])
            node.left = helper(start, node_idx - 1)
            node.right = helper(node_idx + 1, end)
            return node

        return helper(0, n - 1)

    @classmethod
    def construct_tree_ino_postorder(cls, inorder, postorder):
        mapping = cls.__ino_idx_to_idx(pre_post=postorder, inorder=inorder)
        n = len(inorder)

        def helper(start, end):
            if start == end:
                return cls.Node(inorder[start])
            if end < start or start > end:
                return None

            node_idx = -1
            post_idx = -1
            """
                post order will have root at right. 
                So the rightmost in the inorder range given is root node of subtree defined by [start, end]
            """
            for in_idx in range(start, end + 1):
                if post_idx < mapping[in_idx]:
                    node_idx = in_idx
                    post_idx = mapping[in_idx]

            node = cls.Node(inorder[node_idx])
            node.left = helper(start, node_idx - 1)
            node.right = helper(node_idx + 1, end)
            return node

        return helper(0, n - 1)

    @classmethod
    def is_equal(cls, tree1, tree2):
        if not (tree1 and tree2 and tree1.val == tree2.val):
            return False
        left = cls.is_equal(tree1.left, tree2.left)
        right = cls.is_equal(tree1.right, tree2.right)
        return left and right


def init():
    tree1 = Tree.construct_tree_ino_postorder(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
    tree2 = Tree.construct_tree_ino_preorder(inorder=[9, 3, 15, 20, 7], preorder=[3, 9, 20, 15, 7])

    if Tree.is_equal(tree1, tree2):
        raise Exception('Trees are not equal')
    return 1
