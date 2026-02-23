'''
Easy
Topics
premium lock icon
Companies
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            d1 = helper(node.left)
            if d1 == -1:
                return -1
            d2 = helper(node.right)
            if d2 == -1:
                return -1
            return max(d1,d2) + 1 if abs(d1-d2) <= 1 else -1
        return helper(root) != -1 
                
        
            
            
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            ld = dfs(node.left)
            if ld == -1:
                return -1
            rd = dfs(node.right)
            if rd == -1:
                return -1
            if abs(ld - rd) > 1 :
                return -1
            else:
                return max(ld,rd) + 1
        rs = dfs(root)
        return False if rs == -1 else True
