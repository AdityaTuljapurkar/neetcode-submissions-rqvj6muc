from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ds = []
        def view(node ,  level) : 
            if not node  : 
                return  
            if level == len(ds):
                ds.append(node.val)
            
            if node.right : 
                view(node.right,level=level+1)
            if node.left : 
                view(node.left , level=level+1)
        view(root, 0)    
        return ds 
        