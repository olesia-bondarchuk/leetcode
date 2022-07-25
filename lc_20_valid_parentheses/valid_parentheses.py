class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {
            '(' : ')',
            '{': '}',
            '[': ']'
        }
        stack_len = 0

        for char in s:
            if char in parentheses_map:
                stack.append(char)
                stack_len+=1
                continue
            if stack_len == 0:
                return False
            last = stack.pop()
            stack_len-=1
            if parentheses_map[last] != char:
                return False
        return stack_len == 0
