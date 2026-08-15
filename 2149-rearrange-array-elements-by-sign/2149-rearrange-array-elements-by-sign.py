class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p=[]
        neg=[]
        for i in range(n):
            if nums[i]>=0:
                p.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range(len(p)):
            nums[i*2] = p[i]
            nums[(i*2)+1]= neg[i]
        return nums