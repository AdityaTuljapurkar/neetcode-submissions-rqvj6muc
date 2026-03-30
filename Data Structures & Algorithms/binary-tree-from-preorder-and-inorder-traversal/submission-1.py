class Solution:
    def buildTree(self, preorder, inorder):
        # ✅ FIX: You created this correctly, but didn’t use it earlier
        hash_inorder = {val: i for i, val in enumerate(inorder)}

        def helper(pre_start, pre_end, in_start, in_end):
            # ✅ FIX: Base condition was fine, just cleaner this way
            if pre_start > pre_end or in_start > in_end:
                return None

            # ✅ ROOT: preorder always gives root at pre_start
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # ❌ YOUR MISTAKE:
            # local_left = inorder[inorder[local_root]-1]
            # You treated VALUE as INDEX (this is illegal logic)
            
            # ✅ FIX: Use hashmap to find index of root in inorder
            in_root = hash_inorder[root_val]

            # ❌ YOUR MISTAKE:
            # You never calculated size of left subtree
            
            # ✅ FIX: This is the MOST IMPORTANT LINE
            nums_left = in_root - in_start

            # ❌ YOUR MISTAKE:
            # build_left and build_right used random values (local_left, local_right)
            # instead of subtree size

            # ✅ FIX: Correct left subtree
            root.left = helper(
                pre_start + 1,                  # next element after root
                pre_start + nums_left,          # limit using left subtree size
                in_start,
                in_root - 1
            )

            # ❌ YOUR MISTAKE:
            # You didn’t attach left/right to root at all

            # ✅ FIX: Correct right subtree
            root.right = helper(
                pre_start + nums_left + 1,
                pre_end,
                in_root + 1,
                in_end
            )

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)