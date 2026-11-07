class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        l,r = 1,1
        res=[1]*n
        for i in range(0,n):
            res[i]*=l
            l*=nums[i]
            res[n-1-i]*=r
            r*=nums[n-1-i]
        return res