from typing import Optional, List
from helpers.tree_node import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.appendInOrder(root, output)

        return output

    def appendInOrder(self, root, output):
        if root is None:
            return

        self.appendInOrder(root.left, output)
        output.append(root.val)
        self.appendInOrder(root.right, output)
