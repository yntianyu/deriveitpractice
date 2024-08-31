# Given the root node of a tree root, clone the tree, and return the root node of the cloned tree.

# A "cloned tree" is defined as an exact copy. When you modify the cloned tree, it should have no effect on the original tree. This means that you can't simply return the original root node as the solution to the problem.


"""
# Here's the definition of a TreeNode:
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


def cloneTree(root):
    if root is None:
        return

    clonedRoot = TreeNode(root.val)
    clonedRoot.left = cloneTree(root.left)
    clonedRoot.right = cloneTree(root.right)

    return clonedRoot

# Time complexity: O(n)
# Space complexity: O(n) due to recursion stack