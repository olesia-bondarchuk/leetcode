from typing import Optional, List
from helpers.tree_node import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        output = []
        stack = [root]
        postorder = []

        while len(stack) != 0:
            cur = stack.pop()
            postorder.append(cur.val)
            if cur.left is not None:
                stack.append(cur.left)
            if cur.right is not None:
                stack.append(cur.right)

        while len(postorder) != 0:
            output.append(postorder.pop())

        return output
