# Given the root node of a binary tree root, find the rightmost leaf node in the tree, and return its horizontal location.

 
# Here's the definition of a TreeNode:
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightmostLocation(root):
    loc = float("-inf")

    def travel(node, hor):
        if not node:
            return

        if not node.left and not node.right:
            nonlocal loc
            loc = max(hor, loc)

        travel(node.left, hor - 1)
        travel(node.right, hor + 1)
    
    travel(root, 0)
    return loc


rightmostLocation(TreeNode.of([1, 1, 1, 1, None, 1]))
rightmostLocation(TreeNode.of([1]))
rightmostLocation(TreeNode.of([1, 1, 1]))

# Time complexity: O(n)
# Space complexity: O(n)
