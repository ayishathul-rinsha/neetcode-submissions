# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m=0
        def maxDia(root:Optional[Treenode])-> int:
            nonlocal m
            if root:
                l=maxDia(root.left)
                r=maxDia(root.right)
                m=max(m,l+r)
                return 1+max(l,r)
            return 0
        
        maxDia(root)

        return m