class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n-2):
            l=i+1
            r=n-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                t = nums[i] + nums[l] + nums[r]

                if t <0:
                    l+=1
                elif t >0:
                    r-=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1

                    while l <r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
        return ans
