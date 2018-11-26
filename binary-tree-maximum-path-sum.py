# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    globalsum=-float('inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findpathsum(root)
        return self.globalsum
    
    def findpathsum(self, root):
        if not root:
            return 0
        leftsum=max(0,self.findpathsum(root.left))
        rightsum=max(0,self.findpathsum(root.right))
        root_sum = max(leftsum, rightsum,leftsum+rightsum) + root.val
        self.globalsum= max(self.globalsum, root_sum)
        return  root.val + max(0,leftsum, rightsum) 
