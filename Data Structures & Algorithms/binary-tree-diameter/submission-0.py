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
        height = {}
        def cal_height(root: Optional[TreeNode], height: dict) -> int:
            if not root:
                return -1
            left_height = cal_height(root.left, height)
            right_height = cal_height(root.right, height)
            curr_height = max(left_height, right_height) + 1
            height[root] = curr_height
            return curr_height
        cal_height(root, height)
        stack = []
        max_diameter = 0
        stack.append(root)
        while stack:
            node = stack.pop()
            diameter = height.get(node.left, -1) + height.get(node.right, -1) + 2
            max_diameter = max(diameter, max_diameter)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return max_diameter

        

