import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = dict()
        for v in nums:
            dt[v] = dt.get(v, 0) + 1
        print(dt)

        prior_heap = []

        for key, value in dt.items():
            heapq.heappush(prior_heap, (-value, key)) #making it a max heap
        
        counter = 0
        lst = list()
        while counter < k:
            priority, item = heapq.heappop(prior_heap)
            lst.append(item)
            counter+=1

        return lst
