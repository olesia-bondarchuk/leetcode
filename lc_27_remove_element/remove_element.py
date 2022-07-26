from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == val:
                del nums[i]
                l -= 1
            else:
                i+=1

        return l
