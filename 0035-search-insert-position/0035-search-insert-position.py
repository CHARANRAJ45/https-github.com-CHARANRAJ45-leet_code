class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l ,h = 0 , n-1
        lb =n
        while l<=h:
            mid =(l+h)//2
            if nums[mid] >= target:
                lb=mid
                h = mid-1
            else:
                l=mid+1
        return lb