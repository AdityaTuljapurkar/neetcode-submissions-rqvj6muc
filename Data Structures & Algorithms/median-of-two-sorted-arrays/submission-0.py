class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1 , num2 = nums1 , nums2 
        #always binary seach the smaller array 
        if len(num1) > len(num2):
            num1 , num2 = num2 , num1  
        total = len(num1) + len(num2)
        half = total // 2 
        l = 0 
        r = len(num1)-1
        while True : 
            mid1 = (l + r)//2 
            mid2 = half - mid1 - 2 

            #left prtition
            num1_left = num1[mid1] if mid1 >= 0 else float('-inf')
            num2_left = num2[mid2] if mid2 >= 0 else float('-inf')

            #right partition 
            num1_right = num1[mid1+1] if mid1 +1 < len(num1) else float('inf')
            num2_right = num2[mid2+1] if mid2 +1 < len(num2) else float('inf')

            #what is True value 
            if num1_left <= num2_right and num2_left <= num1_right : 
                #for odd number : 
                if total %2 : 
                    return min(num1_right , num2_right)
                #for odd number 
                return (min(num1_right , num2_right) + max(num1_left , num2_left))/2 
            elif num1_left > num2_right : 
               r = mid1 - 1 
            else : 
                l = mid1 +1 

            

