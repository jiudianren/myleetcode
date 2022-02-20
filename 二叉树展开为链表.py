# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root:TreeNode):
        if not root:
            return 
        if self.head:
            self.head.left =None
            self.head.right = root
            self.head =root
        else:
            self.head = root
        tl = root.left
        tr = root.right
        if tl :
            self.dfs(tl)
        if tr:
            self.dfs(tr)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.head = None
        self.dfs(root)
