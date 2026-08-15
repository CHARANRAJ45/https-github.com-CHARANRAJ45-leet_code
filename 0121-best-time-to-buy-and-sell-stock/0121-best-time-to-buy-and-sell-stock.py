class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_p = float('inf')
        max_p = 0
        for i in range(n):
            min_p = min(min_p,prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p