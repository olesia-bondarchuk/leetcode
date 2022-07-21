from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map={}
        for index in range(len(nums)):
            if target - nums[index] in index_map:
                return [index_map[target - nums[index]], index]

            index_map[nums[index]] = index

        return []
    