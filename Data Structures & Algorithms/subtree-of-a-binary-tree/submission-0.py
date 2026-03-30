class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checker(p, q):
            # 1. Both are None? They match!
            if not p and not q:
                return True
            # 2. Safety: One is None or values don't match? No match.
            if not p or not q or p.val != q.val:
                return False
            
            # 3. If we are here, p.val == q.val is true
            res = True 

            # 4. Check the left pair AND the right pair
            return res and checker(p.left, q.left) and checker(p.right, q.right)

        def searcher(node, subnode):
            if not node:
                return False

            # Check if subtree starts HERE
            if checker(node, subnode):
                return True
            
            # If not, use the SEARCHER to keep looking deeper
            return searcher(node.left, subnode) or searcher(node.right, subnode)

        return searcher(root, subRoot)