# Given the root node of a binary tree root, turn the tree into its mirror image. This is also called "inverting" the tree.

# You should modify the tree in-place, and should not return anything.

def invertAll(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left
    invertAll(root.left)
    invertAll(root.right)

# Time complexity: O(n)
# Space complexity: O(n) due to recursion stack