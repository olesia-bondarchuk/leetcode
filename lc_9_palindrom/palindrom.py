class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = []
        while x != 0:
            l.append(x % 10)
            x = int(x / 10)
        for i in range(int(len(l)/2)):
            first = l[i]
            last = l[len(l)-i-1]
            if first != last:
                return False

        return True
