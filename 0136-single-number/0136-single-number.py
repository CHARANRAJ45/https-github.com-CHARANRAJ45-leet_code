class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in range(0,len(nums)):
            a ^= nums[i]
            i+=1
        return a