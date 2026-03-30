class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        values = list(zip(position, speed))
        values.sort(key=lambda x: x[0], reverse=True)  # closest first

        stack = []
        for pos, speed in values:
            val = (target - pos) / speed
            stack.append(val)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()   # merge fleets

        return len(stack)
