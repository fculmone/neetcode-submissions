class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res_stack = []
        for token in tokens:
            if token in "+-*/":
                num2 = int(res_stack.pop())
                num1 = int(res_stack.pop())
                if token == "+":
                    res_stack.append(num1 + num2)
                elif token == "-":
                    res_stack.append(num1 - num2)
                elif token == "*":
                    res_stack.append(num1 * num2)
                elif token == "/":
                    res_stack.append(int(num1 / num2))
            else:
                res_stack.append(int(token))
        return res_stack[0]