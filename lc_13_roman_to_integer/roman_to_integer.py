class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if len(s) == 0:
            return -1

        result = 0
        for i in range(len(s)-1, -1, -1):
            if self.need_to_substract(s, i):
                result = result - roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]

        return result

    def need_to_substract(self, s, i):
        return i < len(s)-1 and ((s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'))
                or (s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'))
                or (s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')))
