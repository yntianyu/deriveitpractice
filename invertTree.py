# Given the root node of a binary tree root, turn the tree into its mirror image. This is also called "inverting" the tree.

# You should modify the tree in-place, and should not return anything.


# Here's the definition of a TreeNode:
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def invertAll(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left
    invertAll(root.left)
    invertAll(root.right)

invertAll(TreeNode.of([1, 2, 3, None, None, None, 4]))
invertAll(TreeNode.of([1, 2]))
invertAll(TreeNode.of([1, None, 2]))

# Time complexity: O(n)
# Space complexity: O(n) due to recursion stack