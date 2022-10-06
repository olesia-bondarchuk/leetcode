from typing import Optional
from helpers.tree_node import TreeNode

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.build_tree_string(root)

    def build_tree_string(self, root):
        if root is None:
            return ''

        result = f'{root.val}'

        if root.left is None and root.right is None:
            return result

        result += f'({self.build_tree_string(root.left)})'
        if root.right is not None:
            result += f'({self.build_tree_string(root.right)})'

        return result
