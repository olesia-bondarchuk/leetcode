from typing import Optional
from helpers.tree_node import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.treeDepth(root)

    def treeDepth(self, root):
        if root is None:
            return 0
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)

        return max(left, right) + 1
