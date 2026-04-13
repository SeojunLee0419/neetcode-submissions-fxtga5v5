class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights)-1
        maxArea = []

        while l<r: 
            area = (r-l) * min(heights[l], heights[r])
            maxArea.append(area)

            if heights[l] - heights[r] > 0: 
                r-= 1
            elif heights[l] - heights[r] <= 0:
                l += 1
        
        return max(maxArea)