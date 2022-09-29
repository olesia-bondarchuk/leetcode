from typing import Optional, List
from helpers.tree_node import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        cur = root
        stack = []

        while cur is not None or len(stack) != 0:
            while cur is not None:
                stack.append(cur)
                output.append(cur.val)
                cur = cur.left

            cur = stack.pop()
            cur = cur.right
