class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        map=defaultdict(int)
        for i,c in enumerate(s):
            map[s[i]]+=1
            map[t[i]]-=1
        for v in map.values():
            if v!=0 : return False
        return True