class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]

        def solve(idx,sub):
            if idx >= len(nums):
                res.append(list(sub))
                return res
            sub.append(nums[idx])
            solve(idx+1, sub)
            sub.pop()
            solve(idx+1,sub)
        solve(0,[])
        return res

        