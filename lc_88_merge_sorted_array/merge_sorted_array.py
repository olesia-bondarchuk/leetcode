from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return
        k = m + n - 1
        i = m - 1
        j = n - 1

        while k >= 0:
            if j < 0 or (nums1[i] > nums2[j] and i >= 0):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
