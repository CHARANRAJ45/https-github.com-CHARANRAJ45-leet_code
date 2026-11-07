class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_m = {0:1}
        c=t=0
        for i in nums:
            t+=i
            if t-k in hash_m:
                c+=hash_m[t-k]
            hash_m[t] = hash_m.get(t,0)+1
        return c