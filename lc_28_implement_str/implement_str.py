class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if haystack == '':
            return -1

        for i in range(len(haystack)-len(needle) + 1):
            stopped_in_advance = False
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    stopped_in_advance = True
                    break

            if not stopped_in_advance:
                return i
        return -1
