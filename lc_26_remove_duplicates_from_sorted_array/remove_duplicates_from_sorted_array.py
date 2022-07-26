class Solution:
    def removeDuplicates(self, nums) -> int:
        list_l = len(nums)
        i = 1
        while i < list_l:
            if nums[i] == nums[i-1]:
                del nums[i]
                list_l -= 1
            else:
                i+=1

        return list_l
