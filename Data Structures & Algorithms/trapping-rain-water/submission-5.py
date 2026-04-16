class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0
        for i, val in enumerate(height):
            if i == 0 or i == len(height)-1:
                continue
            
            left_arr = height[:i]
            right_arr = height[i+1:]
            left_max = max(left_arr)
            right_max = max(right_arr)
            
            if left_max > val and right_max>val:
                minn = min(left_max, right_max)
                water+= minn - val
            
        return water