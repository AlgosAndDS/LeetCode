class Solution(object):
    def isValid(self, s):
        stack = []
        closed_open = {
            ")":"(",
            "}":"{",
            "]":"["
            }
        for char in s:
            if char in closed_open:
                if stack and stack[-1] == closed_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            False