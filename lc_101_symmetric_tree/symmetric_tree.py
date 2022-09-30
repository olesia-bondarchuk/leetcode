from typing import Optional
from helpers.tree_node import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.symmetricTree(root.left, root.right)

    def symmetricTree(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val != right.val:
            return False
        if not self.symmetricTree(left.left, right.right):
            return False
        if not self.symmetricTree(left.right, right.left):
            return False

        return True
