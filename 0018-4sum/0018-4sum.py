class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        my = set()
        for i in range(0,n):
            for j in range(i+1,n):
                hash_set = set()
                for k in range(j+1,n):
                    fourth = target - (nums[i]+nums[j]+nums[k])
                    if fourth in hash_set:
                        temp = [nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        my.add(tuple(temp))
                    hash_set.add(nums[k])
        res =[]
        for ans in my:
            res.append(list(ans))
        return res



                   