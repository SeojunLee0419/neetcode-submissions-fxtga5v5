class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        pref[0] = 1
        
        copy_num = nums.copy()
        copy_num.reverse()

        rev_num = copy_num
        suff[0] = 1
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
            suff[i] = suff[i-1] * rev_num[i-1]

        suff.reverse()

        print(pref)
        print(suff)
        new_nums = []
        for i in range(len(nums)):
            new_nums.append(pref[i]*suff[i])

        print(new_nums)
        return new_nums