class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(openC, closeC):
            if openC == closeC == n:
                result.append("".join(stack))
                return
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closeC)
                stack.pop()
            if closeC < openC:
                stack.append(")")
                backtrack(openC, closeC + 1)
                stack.pop()

        backtrack(0, 0)
        return result

        