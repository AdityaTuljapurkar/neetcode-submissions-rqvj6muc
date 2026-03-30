# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root , float('-inf'), float('inf'))
    def validate (self,Root , minVal ,maxVal ): 
        if Root is None : 
            return True
        if Root.val <= minVal or Root.val >= maxVal:
            return False 
        return (
            self.validate(Root.left ,minVal , Root.val) and self.validate(Root.right , Root.val , maxVal)
        )