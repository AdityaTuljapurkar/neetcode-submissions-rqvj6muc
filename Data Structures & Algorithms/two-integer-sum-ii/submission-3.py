class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # as the array is soerted so we can ues two pointer 
        left = 0 
        right = len(numbers)-1
        while left < right : 
            if numbers[left] + numbers[right] > target :
                right -=1 
            elif numbers[left] + numbers[right] < target :
                left +=1 
            else : 
                return [left+1 , right+1] 

