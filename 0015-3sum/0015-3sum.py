class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        for i in range(0,len(nums)):
            my_set = set()
            for j in range(i+1,len(nums)):
                third = -(nums[i]+nums[j])
                if third in my_set:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    res.add(tuple(temp))
                my_set.add(nums[j])
        return [list(ans) for ans in res]