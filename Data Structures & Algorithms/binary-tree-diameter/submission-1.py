# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# For any node in a tree, the longest path that goes through it is: height of left subtree + height of right subtree
from collections import defaultdict

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root: 
                return -1
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            
            res = max(left_height + right_height + 2, res)

            curr_height = max(left_height, right_height) + 1
            return curr_height
        dfs(root)
        return res

        

