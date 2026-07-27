# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        levels = deque()

        if root is None:
            return ans
        q.append(root)
        level = 0
        levels.append(level)

        while q:
            node = q.popleft()
            level = levels.popleft()
            if level >= len(ans):
                ans.append([node.val])
            else:
                ans[level].append(node.val)

            if node.left is not None:
                q.append(node.left)
                levels.append(level + 1)
            if node.right is not None:
                q.append(node.right)
                levels.append(level + 1)
        return ans
