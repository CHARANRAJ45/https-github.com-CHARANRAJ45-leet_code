class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        slist = [num**2 for num in nums]
        slist.sort()
        return slist
        