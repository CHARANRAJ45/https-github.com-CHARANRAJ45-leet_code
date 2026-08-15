class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash_map ={}
        for i in range(0,n):
            r = target - nums[i]
            if r in hash_map:
                return [hash_map[r],i]
            hash_map[nums[i]] =i