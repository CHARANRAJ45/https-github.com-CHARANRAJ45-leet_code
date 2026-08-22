class Solution:
    def solve(self, idx, tot, brackets, result):
        if idx >= len(brackets):
            if tot == 0:
                result.append("".join(brackets))
            return
        if tot > len(brackets) // 2:
            return
        elif tot < 0:
            return
            
        brackets[idx] = "("
        self.solve(idx + 1, tot + 1, brackets, result)
        
        brackets[idx] = ")"
        self.solve(idx + 1, tot - 1, brackets, result)

    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""] * (n * 2)
        result = []
        self.solve(0, 0, brackets, result)
        return result