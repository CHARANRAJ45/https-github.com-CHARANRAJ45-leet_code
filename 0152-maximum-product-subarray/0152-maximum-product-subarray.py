class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        c_ma, c_mi = 1, 1
        
        for i in nums:
            # If we encounter a 0, the current sub-products reset to 1
            if i == 0:
                c_ma, c_mi = 1, 1
                res = max(res, 0)
                continue
                
            # If negative, max and min swap roles
            if i < 0:
                c_ma, c_mi = c_mi, c_ma
                
            c_ma = max(i, i * c_ma)
            c_mi = min(i, i * c_mi)
            
            res = max(res, c_ma)
            
        return res