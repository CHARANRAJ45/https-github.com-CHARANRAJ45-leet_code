class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r =[0] *n
        p=0
        neg=1
        for i in range(n):
            if nums[i]>0:
                r[p] = nums[i]
                p+=2
            else:
                r[neg] = nums[i]
                neg+=2
        return r  
