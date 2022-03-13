class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if (not A) or (not B):
            return False
        cur = self.recur(A,B)
        if cur:
            return True
        cur_left = self.isSubStructure(A.left,B)
        cur_right = self.isSubStructure(A.right,B)
        if cur_left or cur_right:
            return True
        return False

    def recur(self, A: TreeNode, B: TreeNode) -> bool:
        if not B: return True
        if not A or A.val != B.val: return False
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)
