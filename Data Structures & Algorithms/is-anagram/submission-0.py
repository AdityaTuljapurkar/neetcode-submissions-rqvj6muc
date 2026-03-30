class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using array indxing using 32 size array 
        if len(s) != len(t) : return False 
        s_array = 26*[0]
        t_array = 26*[0]
        for i in range(len(s)):
            s_array[ord(s[i])-97] +=1 
            t_array[ord(t[i])-97] +=1 
        
        return True if s_array == t_array else False
        