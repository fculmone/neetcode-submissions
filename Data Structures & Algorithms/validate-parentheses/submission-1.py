class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                open_bracket = stack.pop()
                close_bracket = bracket
                if (open_bracket == '(' and close_bracket == ')' or
                    open_bracket == '{' and close_bracket == '}' or
                    open_bracket == '[' and close_bracket == ']'):
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False