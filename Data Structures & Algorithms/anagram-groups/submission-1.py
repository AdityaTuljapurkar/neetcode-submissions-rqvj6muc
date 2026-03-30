class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 3using group anagram 
        #not sorted , no order is required  
        hashSet = {}
        #creating a frequency table for hahset 
        compare_array = []

        for word in strs :
            freq_array = [0]*26
            for letters in word : 
                freq_array[ord(letters)-97]+=1 
            compare_array.append(tuple(freq_array))

        for i , val  in enumerate(compare_array) :
            if val in hashSet : 
                hashSet[val].append(strs[i])
            else : 
                hashSet[val] = [strs[i]]
        
        return list(hashSet.values())


