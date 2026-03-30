class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Both are None? Success!
        if not p and not q:
            return True
        if not p or not q : 
            return False
        if p.val != q.val:
            return False
            

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)