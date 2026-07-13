class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        else:
            openparentheses = {'[' : ']', '(' : ')', '{' : '}'}
            closeparentheses = {']' : '[', ')' : '(', '}' : '{'}
            stack = []
            for i, c in enumerate(s):
                # check if first char is closing parentheses
                if i == 0 and c in closeparentheses:
                    return False
                
                #check if the character is not parentheses at all
                if c not in openparentheses and c not in closeparentheses:
                    continue
                # check if the char is open parentheses, then push to stack
                elif c in openparentheses:
                    stack.append(c)
                #char is in closeparentheses
                else:
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == closeparentheses[c]:
                        stack.pop()
                    else:
                        return False
            
            return len(stack) == 0


