class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 
        #index , value
        for i , h in enumerate(heights) : 
            start = i
            while stack and stack[-1][1] > h : 
                idex , val = stack.pop()
                maxArea = max(maxArea, val * (i - idex)) 
                start = idex 
            stack.append((start , h))

        for i , h in stack : 
            maxArea = max(maxArea , h*(len(heights)-i))
        return maxArea             

        