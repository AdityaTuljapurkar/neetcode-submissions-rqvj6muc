class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #as the array is not sorted use hashmap  
        seen = {}
        for i , num in enumerate(nums):
            need =  target - num 
            if need in seen : 
                return [seen[need],i]
            seen[num] = i