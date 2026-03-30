class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #using prefix and suffix product as a optimal appoch 
        preProduct = [1]*len(nums)
        pre = 1 
        for i in range(len(nums)):
            if i == 0 : 
                preProduct[i] = 1 
            else : 
                pre*=nums[i-1] 
                preProduct[i] = pre 
        
        postProduct = [1]*len(nums)
        post = 1
        for i in range(len(nums)-1 , -1,-1) :
            if i == len(nums)-1 : 
                postProduct[i] = 1 
            else : 
                post *= nums[i+1]
                postProduct[i] = post 
        
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = postProduct[i]*preProduct[i]
        return res 

                
        
            
        