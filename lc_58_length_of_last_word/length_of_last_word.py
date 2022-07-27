class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return -1
        count = 0
        is_space = False
        for i in range(len(s)-1, -1,-1):
            if s[i] == ' ' and count > 0:
                is_space = True
            elif 'a' <= s[i].lower() <= 'z' and not is_space:
                count += 1

        return count
