class Solution:
    def trap(self, height: List[int]) -> int:
        

        leftmax=[]
        max = None
        for i,v in enumerate(height):
            if max is None or v> max:
                max = v
            leftmax.append(max)

        rightmax = []
        max = None
        
        for i,v in enumerate(reversed(height)):
            if max is None or v > max:
                max = v
            rightmax.append(max)

        rightmax.reverse()


        print(leftmax)
        print(rightmax)

        watertotal = 0

        for index,floor in enumerate(height):
            maxheight = min(leftmax[index],rightmax[index])-floor
            if (maxheight > 0):
                watertotal+=maxheight


        
        # water = 0
        # for i, val in enumerate(height):
        #     if i == 0 or i == len(height)-1:
        #         continue
            
        #     if val < height[i-1] and val < height[i+1]:
        #         water+= min(height[i-1], height[i+1]) - val
        #         print(water)

        
        return watertotal