from typing import Optional, List
from helpers.tree_node import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        cur = root
        stack = []

        while cur is not None or len(stack) != 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            output.append(cur.val)
            cur = cur.right

        return output
