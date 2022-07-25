class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) == 0:
    #         return ''
    #     prefix = strs[0]
    #     max_prefix_len = len(strs[0])
    #     for k in range(1, len(strs)):
    #         count = 0
    #         for i in range(max_prefix_len):
    #             if i >= len(strs[k]):
    #                 break
    #             if prefix[i] != strs[k][i]:
    #                 break
    #             count += 1
    #         max_prefix_len = count
    #     return prefix[0:max_prefix_len]

    def longestCommonPrefix(self, strs):
        longest_prefix = strs[0]
        for word in strs:
            prefix = ''
            for c1,c2 in zip(word, longest_prefix):
                if c1 == c2:
                    prefix += c1
                else:
                    break
            longest_prefix = prefix
        return prefix
