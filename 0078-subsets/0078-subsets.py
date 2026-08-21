class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        t_s = 1 << n
        ans = []
        for num in range(0, t_s):
            lis = []
            for i in range(0, n):
                if num & (1 << i) != 0:
                    lis.append(nums[i])  # Changed num[i] to nums[i]
            ans.append(lis)
        return ans