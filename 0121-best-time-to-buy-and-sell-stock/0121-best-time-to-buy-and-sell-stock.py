class Solution(object):
    def maxProfit(self, prices):
        l,r = 0,1
        maxp=0
        while r!=len(prices):
            if prices[r] > prices[l]:
                prf = prices[r] - prices[l]
                maxp = max(maxp,prf)
            else:
                l=r
            r+=1
        return maxp