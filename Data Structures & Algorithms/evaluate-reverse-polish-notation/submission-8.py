import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Operations = {
            '+': lambda left, right: left + right,
            '-': lambda left, right: left - right,
            '*': lambda left, right: left * right,
            '/': lambda left, right: int(left / right),
        }
        
        stk = []
        for t in tokens:
            if t not in Operations:
                stk.append(t)
            else:
                right = int(stk.pop())
                left = int(stk.pop())
                res = Operations[t](left, right)
                stk.append(res)
        return int(stk[0])