from typing import Optional, List
from helpers.tree_node import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        self.appendPreorder(root, output)

        return output

    def appendPreorder(self, root, output):
        if root is None:
            return

        output.append(root.val)
        self.appendPreorder(root.left, output)
        self.appendPreorder(root.right, output)
