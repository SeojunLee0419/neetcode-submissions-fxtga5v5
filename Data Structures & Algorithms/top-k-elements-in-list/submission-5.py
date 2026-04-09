import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = dict()
        for v in nums:
            dt[v] = dt.get(v, 0) + 1
        print(dt)

        prior_heap = []

        for value, frequency in dt.items():
            heapq.heappush(prior_heap, (-frequency, value)) #making it a max heap
            # if len(prior_heap) > k:
            #     heapq.heappop(prior_heap)
        

        res = []
        for i in range(k):
            #priority, item = heapq.heappop(prior_heap)
            res.append(heapq.heappop(prior_heap)[1])

        return res
