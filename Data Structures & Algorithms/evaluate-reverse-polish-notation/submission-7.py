import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATIONS = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        stack = []
        result = 0

        for t in tokens:
            if t in OPERATIONS:
                right = int(stack.pop())
                left = int(stack.pop())
                result = OPERATIONS[t](left, right)
                stack.append(result)
            else:
                stack.append(t)                    
        
        return int(stack[0])
