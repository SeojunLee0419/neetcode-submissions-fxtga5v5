class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            need = target - j
            if need in seen:
                return [seen[need], i]
            seen[j] = i
        