# Given the root node of a binary tree root, return the height of the tree.


# Here's the definition of a TreeNode:
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    # HINT: height(root) = something here....height(something)

    # 1. find the longest path down in root.left
    # 2. find the longest path down in root.right
    # 3. find the max path length btw root.left and root.right
    # 4. return what you found in 3. + 1 for the root

    if root is None:
        return 0
        
    return max(height(root.left), height(root.right)) + 1


height(TreeNode.of([1, 2, 3, 4, 5, None, 6, None, 7]))
height(TreeNode.of([7]))
height(TreeNode.of([5, 2]))

# Time complexity: O(n)
# Space complexity: O(n) due to recursion stack, use command D to access similar elements
