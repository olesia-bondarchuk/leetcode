from typing import Optional, List
from helpers.tree_node import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        cur = root
        stack = []

        while cur is not None or len(stack) != 0:
            while cur is not None:
                stack.append((cur, 1))
                stack.append((cur, 2))
                cur = cur.left

            cur, option = stack.pop()
            if option == 2:
                cur = cur.right
            else:
                output.append(cur.val)
                cur = None

        return output
