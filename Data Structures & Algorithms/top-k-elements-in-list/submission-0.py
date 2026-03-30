class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creating a hash freq table  
        res = []
        freq = {}
        for i in nums : 
            if i in freq : 
                freq[i] +=1 
            else : 
                freq[i] = 1
        
        for key , value in freq.items() : 
            res.append((key,value))

        res.sort(key=lambda x: x[1], reverse=True)
        return [num for num , _ in res[:k]]