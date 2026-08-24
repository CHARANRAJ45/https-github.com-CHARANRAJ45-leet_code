class Solution:
    def solve(self,idx,subset,result,digits):
        if idx >= len(digits):
            result.append("".join(subset))
            return
        char_map={ "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        for char in char_map[digits[idx]]:
            subset.append(char)
            self.solve(idx+1,subset,result,digits)
            subset.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        self.solve(0,[],result,digits)
        return result