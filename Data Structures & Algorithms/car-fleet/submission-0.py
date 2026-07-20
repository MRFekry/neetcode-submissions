class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedPairs = zip(position, speed)
        sortedPairs = sorted(positionSpeedPairs, reverse=True)

        stack = []
        for p, s in sortedPairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)