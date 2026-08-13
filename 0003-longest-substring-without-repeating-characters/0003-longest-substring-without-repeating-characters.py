class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        r=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    r=max(r,j-i+1)
        return r