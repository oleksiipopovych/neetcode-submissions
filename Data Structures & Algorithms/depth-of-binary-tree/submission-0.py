# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def walk(node, level):
    if node is None:
        return level
    

    return max(walk(node.left, level + 1), walk(node.right, level + 1))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return walk(root, 0)
        