class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)

        if not nums:
            return 0
        longest = 0
        start = int()
        for val in st:
            length = 1
            #continue if val isn't starting number of the contiguous sequence
            if val-1 in st:
                continue
            while (val + 1) in st:
                length+= 1
                val+=1
            longest = max(longest, length)
    

        return longest