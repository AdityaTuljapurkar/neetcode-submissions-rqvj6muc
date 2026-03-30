from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal =  0
        count = 0
        queue = deque([(root , root.val)])
        while queue : 
            
            node , maxVal  = queue.popleft()
            if node.val >= maxVal : 
                count +=1 
                
            if node.left : 
                queue.append((node.left,max(maxVal,node.left.val)))
            if node.right : 
                queue.append((node.right,max(maxVal,node.right.val)))
        return count 