class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = float('inf')
        for i in range(1,len(arr)):
            mindiff=min(mindiff,arr[i]-arr[i-1])
        res=[]
        for i in range(1,len(arr)):
            if (arr[i]-arr[i-1])==mindiff:
                res.append([arr[i-1],arr[i]])
        return res
        
