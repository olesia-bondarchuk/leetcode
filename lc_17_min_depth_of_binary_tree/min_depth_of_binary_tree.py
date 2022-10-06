from typing import Optional
from helpers.tree_node import TreeNode

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_min_tree_depth(root)

    def get_min_tree_depth(self, root):
        if root is None:
            return 0

        left_depth = self.get_min_tree_depth(root.left)
        right_depth = self.get_min_tree_depth(root.right)


        if (left_depth > right_depth and right_depth != 0) or left_depth == 0:
            return 1 + right_depth
        return 1 + left_depth
