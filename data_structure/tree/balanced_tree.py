# AVL tree / Red Black Tree are both impl of balanced BST

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, val):
        # Perform the normal BST insertion
        if not root:
            return TreeNode(key)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        # Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and val < root.left.val:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and val > root.right.val:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

# Example usage
avl = AVLTree()
root = None

keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    root = avl.insert(root, key)

# Preorder Traversal
print("Preorder traversal of the constructed AVL tree is:")
avl.pre_order(root)