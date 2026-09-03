class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                # Check if stack is empty before popping
                if not stack:
                    return False
                ch = stack.pop()
                if (i == ')' and ch == '(') or \
                   (i == ']' and ch == '[') or \
                   (i == '}' and ch == '{'):
                    continue
                else:
                    return False
        return len(stack) == 0