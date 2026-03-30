class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l =  0
        r = len(nums)-1 
        while l <= r : 
            mid = (l+r)//2 
            if target == nums[mid]:
                return mid 
            
            # left sorted array
            if nums[l] <= nums[mid] : 
                # FIX: use AND (target must be inside both bounds)
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1  
                else : 
                    l = mid + 1 
            else : 
                # right sorted array
                # FIX: use AND (target must be inside both bounds)
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1 
                else : 
                    r = mid - 1 
        return -1
