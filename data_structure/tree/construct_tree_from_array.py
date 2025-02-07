class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.tree = None

    def init(self, array):
        self.tree = TreeNode(array[0])
        self.tree.left = self.construct_from_array(array, 1)
        self.tree.right = self.construct_from_array(array, 2)

    def construct_from_array(self, vals, k):
        if k >= len(vals) or vals[k] is None:
            return None

        root = TreeNode(vals[k])
        leftIndex = 2 * k + 1
        root.left = self.construct_from_array(vals, leftIndex)

        rightIndex = 2 * k + 2
        root.right = self.construct_from_array(vals, rightIndex)

        return root


s = Solution()
s.init([0, 0, None, 0, None, 0, None, None, 0])
