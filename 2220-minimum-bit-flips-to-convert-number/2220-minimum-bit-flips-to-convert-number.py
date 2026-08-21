class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = start ^ goal
        c=0
        for i in range(0,32):
            if a & (1<<i) !=0:
                c+=1
        return c
