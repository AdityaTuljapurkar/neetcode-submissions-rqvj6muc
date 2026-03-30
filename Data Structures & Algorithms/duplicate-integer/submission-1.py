class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #using two ponter approch 
        left = 0 
        right = len(nums) -1 
        check = set(nums)
        return True if len(check) != len(nums) else False  
        