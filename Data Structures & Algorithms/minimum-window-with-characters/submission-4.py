class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #how will i track the validity 
        if len(s) < len(t) : 
            return ""
        

        have = 0 
        window = {}
        t_hash = {}
        for i in t : 
            t_hash[i] = 1+ t_hash.get(i,0)
        need = len(t_hash)

        l = r  = 0
        minl = minr = 0
        minlen = float("inf")
        while  r <len(s):
            #what is the validity 
            if need != have and s[r] in t_hash : 
                window[s[r]]  = window.get(s[r],0)+1 
                if window[s[r]] == t_hash[s[r]]:
                    have += 1 
            #whaat if invalid 
            while have == need :
            #count for the return value 
                temp = (r-l)+1
                if minlen > temp :
                    minl = l 
                    minr = r
                    minlen = (r-l)+1
                if s[l] in window :
                    window[s[l]] =  window.get(s[l])-1 
                    if window[s[l]] < t_hash[s[l]] : 
                        have -=1 
                l+=1 

            r+=1 
        return "".join(s[minl:minr+1]) if minlen != float("inf") else ""


        



                    