class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = { "+", "-", "*","/"}
        stack = []
        for i in tokens :
            val = 0 
            if i in oper : 
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if i == "+":
                    val = val1+val2
                elif i == "-":
                    val = val2-val1
                elif i == "*":
                    val = val1*val2
                else : 
                    val = int(val2/val1 )
                stack.append(val)
                continue
            else : 
                stack.append(i)
        return int(stack[-1])