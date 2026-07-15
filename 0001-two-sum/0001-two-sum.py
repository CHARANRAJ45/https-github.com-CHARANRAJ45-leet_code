class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        n=len(nums)
        for i,num in enumerate(nums):
            compliment=target-num
            if compliment in num_map:
                temp= [i,num_map[compliment]]
                temp.sort()
                return temp
            num_map[num]=i