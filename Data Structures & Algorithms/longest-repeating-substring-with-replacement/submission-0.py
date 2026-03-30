class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqhash =  {}
        l =0 
        r = 0 

        maxlength = 0 
        for r in  range(0,len(s)):
            freqhash[s[r]] = 1+freqhash.get(s[r],0)
            while (r-l+1) - max(freqhash.values()) > k :
                freqhash[s[l]] -=1 
                l+=1
            
            maxlength  = max(maxlength , r-l+1)

        return maxlength
