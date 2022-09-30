from typing import Optional
from helpers.tree_node import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.treeIdentical(p, q)

    def treeIdentical(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False

        if tree1.val != tree2.val:
            return False
        if not self.treeIdentical(tree1.left, tree2.left):
            return False
        if not self.treeIdentical(tree1.right, tree2.right):
            return False

        return True
