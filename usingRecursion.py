# Given the root node of a binary tree root, return the number of nodes in the tree.

"""
# Here's the definition of a TreeNode:
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

def numNodes(root):

    if root is None:
        return 0
    # your code goes here
    return 1 + numNodes(root.right) + numNodes(root.left)


numNodes(TreeNode.of([1]))
numNodes(TreeNode.of([1, 2]))
numNodes(TreeNode.of([1, 2, 3]))

# Time complexity: O(n)
# Space complexity: O(n)
