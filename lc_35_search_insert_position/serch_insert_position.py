class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low = 0
        high = len(nums)-1
        return self.search(nums, target, low, high)

    def search(self, nums, target: int, low: int, high: int) -> int:
        if nums is None:
            return -1
        if target is None:
            return -1

        if high >= low:
            #mid = low + (high - low) // 2
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return self.search(nums, target, low, mid-1)
            return self.search(nums, target, mid+1, high)
        return low
