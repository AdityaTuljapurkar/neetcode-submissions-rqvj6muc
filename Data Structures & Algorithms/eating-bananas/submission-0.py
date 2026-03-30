class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Koko Eating Bananas 
        r = max(piles)
        res = r
        l = 1 
        while l<= r :
            hrs = 0 
            mid = (l+r)//2 
            for i in piles : 
               hrs += math.ceil(i/mid)
            if hrs > h : 
                l = mid+1 
            else : 
                res = min(mid,res)
                r = mid-1 
        return res 
            
