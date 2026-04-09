import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = dict()
        for v in nums:
            dt[v] = dt.get(v, 0) + 1
    
        heap = []
        
        for value, frequency in dt.items():
            heapq.heappush(heap, (frequency, value))
            if len(heap) > k:
                heapq.heappop(heap) #removes the least occuring from the heap que 
        
        sol = list()
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
        print(sol)
        return sol
        