class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0 
        seen= set()
        left =0 
        right = 0
        length = right - left+1
        maxlength = length
        while left <= right and right< len(s):
            while s[right] in seen : 
                seen.remove(s[left])
                left +=1 
            

            length = right - left +1
            maxlength  = max(length , maxlength)
            seen.add(s[right])  
            right +=1 
        return maxlength
    
    

            
        
    

            
        