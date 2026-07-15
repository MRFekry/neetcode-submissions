class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        if len(temperatures) == 1: return [0]

        stack = []
        for i, t in enumerate(temperatures):
            rp = i + 1
            steps = 0
            if rp >= len(temperatures):
                stack.append(0)
                break
            while rp < len(temperatures) and t >= temperatures[rp]: 
                steps += 1
                rp += 1
            if rp == len(temperatures) and steps > 0:
                stack.append(0)
            else:
                stack.append(steps + 1)
        return stack