class Solution:
    def lowerbound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, h = 0, n - 1
        lb = -1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] >= target:
                lb = mid
                h = mid - 1
            else:
                l = mid + 1
        return lb

    def upperbound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        ub = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lowerbound(nums, target)
        if lb == -1 or lb >= len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = self.upperbound(nums, target)
        # If upperbound didn't find a strictly greater element, 
        # the last occurrence is at the very end of the array (len(nums) - 1)
        # or the target only appears up to a certain point.
        if ub == -1:
            ub = len(nums) - 1
        else:
            ub -= 1
        return [lb, ub]