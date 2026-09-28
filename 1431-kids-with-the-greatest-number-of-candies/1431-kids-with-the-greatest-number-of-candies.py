class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        length=max(candies)
        l = []
        for i in candies:
            if i+ extraCandies >=length :
                l.append(True)
            else:
                l.append(False)
        return l