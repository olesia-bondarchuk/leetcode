class Solution:
    def plusOne(self, digits):
        if digits == '':
            return -1
        carry_over = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry_over
            if digits[i] > 9:
                digits[i] = 0
            else:
                carry_over = 0
                break

        if carry_over == 1:
            digits[:0] = [carry_over]
        return digits
