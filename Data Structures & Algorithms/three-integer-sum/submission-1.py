class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #using 3 pointer approch to solve in O(n^2)
        res = []
        for i in range(0, len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue 
            left = i+1
            right= len(nums)-1
            while left < right :
                Sum = nums[left]+nums[right] + nums[i]
                if Sum < 0 :
                    left+=1
                elif Sum > 0 :
                    right -=1 
                else : 
                    res.append([nums[i],nums[left],nums[right]])
                    left +=1
                    while nums[left]  == nums[left-1]  and left < right :
                        left +=1

        return res