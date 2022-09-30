from typing import Optional
from helpers.tree_node import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        node = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(node)

        return root
