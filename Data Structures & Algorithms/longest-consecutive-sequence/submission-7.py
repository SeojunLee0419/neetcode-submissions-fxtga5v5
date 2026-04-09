class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums.sort()
        counter = 1
        prev = nums[0]
        print(nums)
        list_of_consc = []
        for i in range(1, len(nums)):
            if nums[i]-prev == 1:
                print(nums[i])
                counter+=1
                prev = nums[i]
            elif nums[i]-prev ==0:
                continue
            else:
                list_of_consc.append(counter)
                counter = 1
                prev = nums[i]
        list_of_consc.append(counter)
        counter = max(list_of_consc)
        return counter