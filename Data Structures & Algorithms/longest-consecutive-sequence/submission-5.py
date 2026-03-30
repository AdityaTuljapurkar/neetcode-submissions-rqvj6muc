class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #using the set for the intial 
        if not nums : return 0
        maxLength =  0 
        seen =  set(nums)
        for i in nums: 
            if i-1 not in nums :
                #this is the first one 
                longest = 1
                n = i 
                while n+1 in seen : 

                    n +=1
                    longest += 1 
                maxLength = max(maxLength , longest)
                    
        return maxLength