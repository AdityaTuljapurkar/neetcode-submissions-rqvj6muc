class Solution:
    def isValid(self, s: str) -> bool:
        #using Stack to trace the condition 
        stack = []
        check = {
            "{":"}",
            "[":"]",
            "(":")",
        }
        for i in s : 
            if stack and stack[-1] in check : 
                if i == check[stack[-1]]:
                    stack.pop()
                    continue
            stack.append(i)

        return False if stack else True
