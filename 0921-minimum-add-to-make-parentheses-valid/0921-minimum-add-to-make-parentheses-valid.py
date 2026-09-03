class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o_b=0
        i=0
        for c in s:
            if c=='(':
                o_b+=1
            elif c==')':
                if o_b >0:
                    o_b-=1
                else:
                    i+=1
        return i+o_b