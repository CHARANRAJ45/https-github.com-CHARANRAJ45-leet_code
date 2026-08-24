class Solution:
    def solve(self,last,tot,subset,result,n,k):
        if tot == n and len(subset) == k:
            result.append(subset.copy())
            return
        if tot > n or len(subset) > k:
            return
        
        for i in range(last,10):
            s =tot+i
            subset.append(i)
            self.solve(i+1,s,subset,result,n,k)
            subset.pop()




    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.solve(1,0,[],result,n,k)
        return result
         