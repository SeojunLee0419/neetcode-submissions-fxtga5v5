class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        reps = len(nums)
        newNums = []
    
        for i in range(reps):
            val = 1
            for j in range(reps):
                if j == i:
                    continue
                val *= nums[j]

            newNums.append(val)

        return newNums