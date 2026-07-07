class Solution(object):
    def sumAndMultiply(self, n):
        digits = [int(c) for c in str(n) if c!='0']
        x = int(''.join(map(str,digits))) if digits else 0
        return x * sum(digits)
        