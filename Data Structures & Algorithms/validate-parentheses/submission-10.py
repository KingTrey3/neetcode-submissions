class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        p_map = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char not in p_map:
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                if p_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) >= 1:
            return False
        else:
            return True
        