from typing import Optional
from helpers.tree_node import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_str = self.build_tree_string(root)
        subroot_str = self.build_tree_string(subRoot)
        print(root_str)
        print(subroot_str)
        try:
            root_str.index(subroot_str)
            return True
        except ValueError:
            return False

    def build_tree_string(self, root):
        if root is None:
            return ''

        result = f'({root.val}'

        if root.left is None and root.right is None:
            return result + ')'

        result += f'({self.build_tree_string(root.left)})'
        result += f'({self.build_tree_string(root.right)})'

        return result + ')'
