class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        data = set(nums)
        last =max(nums)
        first = min(nums)
        maxlength = 0 
        temp = 0
        for i in range(first ,last+1):
            

            if i in data :
                temp +=1 
                maxlength = max(temp , maxlength)
            else : 
                temp = 0
                continue 
        return maxlength