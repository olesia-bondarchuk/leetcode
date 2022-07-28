class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            return self.addBinary(b,a)

        carry_over = 0
        result = ''
        i = len(a)-1
        j = len(b)-1
        while i>=0:
            ai = ord(a[i]) - ord('0')
            bj = 0
            if j >= 0:
                bj = ord(b[j]) - ord('0')

            sum = ai + bj + carry_over
            if sum >= 2:
                result = str(sum-2) + result
                carry_over = 1
            else:
                carry_over = 0
                result = str(sum) + result

            i-=1
            j-=1

        if carry_over == 1:
            result = '1' + result


        return result
