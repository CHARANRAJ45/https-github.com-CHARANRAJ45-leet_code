class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        ls,rs=0,0
        if n==k:
            return sum(cardPoints)
        for i in range(0,k):
            ls +=cardPoints[i]
        m=ls
        r=n-1
        for i in range(k-1,-1,-1):
            ls -= cardPoints[i]
            rs += cardPoints[r]
            m = max(m,ls+rs)
            r-=1
        return m 
        