class Solution:
    def buildTree(self, preorder, inorder):
        hash_inorder = {}
        for i, val in enumerate(inorder):
            hash_inorder[val] = i 

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None 

            # root
            local_root = preorder[pre_start]
            tree_root = TreeNode(local_root)
            root_idx = hash_inorder[local_root]
            #left size 
            left_size = root_idx - in_start


            tree_root.left = helper(
                pre_start + 1,
                pre_start + left_size,
                in_start,
                root_idx - 1
            )

            tree_root.right = helper(
                pre_start + left_size + 1,
                pre_end,
                root_idx + 1,
                in_end
            )

            return tree_root
        
        return helper(0, len(preorder)-1, 0, len(inorder)-1)