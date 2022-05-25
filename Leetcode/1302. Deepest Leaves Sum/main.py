# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        end_point = defaultdict(int)

        def traversal(root, height):
            if root.left == None and root.right == None:
                end_point[height] += root.val
                return
            if root.left != None:
                traversal(root.left, height+1)
            if root.right != None:
                traversal(root.right, height+1)
        traversal(root, 1)

        ans = root.val
        ans_height = 1

        for key, val in end_point.items():
            if ans_height < key:
                ans_height = key
                ans = val
        return ans
