import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #tracking of the valid and invalid 
        maxnum = float('inf')
        res = []
        heap = []
        window = []
        for i in range(0,k):
            window.append(-nums[i])
        l = 0 
        r = k-1
        heapq.heapify(window)
        heap = window
        _max = -heap[0]
        res.append(_max)
        #we will be using while loop for navigating valid and invalid
        while r< len(nums)-1:
            r+=1 
            heapq.heappush(heap,-nums[r])
            heap.remove(-nums[l])
            l+=1
            heapq.heapify(heap)
            _max = -heap[0]
            res.append(_max)

        return res




        

