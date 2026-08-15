class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        e_s=n*(n+1)//2
        s=sum(nums)
        return e_s-s