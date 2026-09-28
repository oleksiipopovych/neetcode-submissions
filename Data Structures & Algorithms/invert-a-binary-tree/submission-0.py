# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def walk(node):
    if node is None:
        return

    left = node.left
    right = node.right

    node.left = right
    node.right = left
    walk(node.left)
    walk(node.right)

    return node
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return walk(root)