class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        m = float('-inf')
        t=0
        for i in range(0,n):
            t = t+nums[i]
            m = max(m,t)
            if t<0:
                t=0
        return m
        