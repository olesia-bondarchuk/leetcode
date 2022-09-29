from typing import Optional, List
from helpers.tree_node import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.appendPostorder(root, output)

        return output

    def appendPostorder(self, root, output):
        if root is None:
            return

        self.appendPostorder(root.left, output)
        self.appendPostorder(root.right, output)
        output.append(root.val)
