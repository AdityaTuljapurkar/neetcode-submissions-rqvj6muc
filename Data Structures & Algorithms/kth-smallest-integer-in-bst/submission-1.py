# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = None  
        count = 0 
        
        def triversal(node): 
            nonlocal value, count
            if node is None or count >= k: 
                return 

            triversal(node.left)
            count +=1 
            if node.val and k == count : 
                value = node.val 
                return 
            
            triversal(node.right) 
        
        triversal(root)
        return value
            

