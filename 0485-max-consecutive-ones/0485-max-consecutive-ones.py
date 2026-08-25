class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        a=0
        for n in nums:
            if n==0:
                c=0
            else:
                c+=1
            a = max(a,c)
        return a
        