class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False 
        s1Freq = { }
        s2Freq = {}
        r = len(s1)-1
        l =0 
        for i in s1 : 
            s1Freq[i] = s1Freq.get(i ,0) +1 
        for i in range(0 , r+1):
            s2Freq[s2[i]] = s2Freq.get(s2[i],0)+1 
        if s1Freq == s2Freq: return True 
        while l<r and r < len(s2)-1 : 
            r+=1
            s2Freq[s2[r]] = s2Freq.get(s2[r],0)+1
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]

            l+=1
            if s1Freq == s2Freq: return True
        return False 