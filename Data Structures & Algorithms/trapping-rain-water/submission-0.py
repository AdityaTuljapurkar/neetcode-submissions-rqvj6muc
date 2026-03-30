class Solution:
    def trap(self, height: List[int]) -> int:
        #trapping rain water question 
        #min(maxleft , maxRight) - h = value 
        # both O(n) 
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)
        tempLeft = 0 
        tempRight = 0 
        for i in range (1 , len(height)) : 
            #maxleft 
            tempLeft = max(height[i-1],tempLeft)
            maxLeft[i] = tempLeft 

        for i in range(len(height)-2,-1,-1):
            
            tempRight= max(tempRight,height[i+1])
            maxRight[i] = tempRight
        
        res = [0]*len(height)
        for i in range(0,len(height)):
            value= min(maxLeft[i], maxRight[i]) - height[i]

            if value > 0 : 
                res[i] = value 
        
        return sum(res)
        

