class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 2
        pprev = 1
        for _ in range(3, n+1):
            temp = prev
            prev = prev + pprev
            pprev = temp
        return prev
            