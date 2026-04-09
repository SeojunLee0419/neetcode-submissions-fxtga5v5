class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #optimal 
        sett = set(nums)
        longest = 0
        for n in sett:
            if(n-1) not in sett:
                
                length = 0
                while (n+length) in sett:
                    length+=1
                longest = max(length, longest)

        return longest
