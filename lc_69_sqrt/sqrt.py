class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        start = 1
        end = x//2
        candidate = 1

        while start <= end:
            middle = (start + end)//2
            if middle*middle == x:
                return middle
            if middle*middle > x:
                end = middle - 1
            elif middle*middle < x:
                start = middle + 1
                if middle > candidate:
                    candidate = middle
        return candidate
                