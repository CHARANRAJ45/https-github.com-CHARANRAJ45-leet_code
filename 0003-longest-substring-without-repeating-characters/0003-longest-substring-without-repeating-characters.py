class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        r=0
        n=len(s)
        maxi=0
        while r<n:
            if s[r] in d:
                l=max(l,d[s[r]]+1)
            maxi=max(maxi,r-l+1)
            d[s[r]]=r
            r+=1
        return maxi