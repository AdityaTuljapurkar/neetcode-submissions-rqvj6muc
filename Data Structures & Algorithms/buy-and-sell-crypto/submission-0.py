class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r =0 
        #using 2 pointer 
        lowest =  0
        while l <=  r and r < len(prices): 
            if prices[l] > prices[r]:
                l =r 
            else  : 
                maxProfit = max(maxProfit , prices[r]-prices[l])
            r+=1
        return maxProfit 