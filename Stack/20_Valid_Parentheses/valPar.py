class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack:
                    if stack.pop() != par[c]:
                        return False
                else:
                    return False
        
        return not stack