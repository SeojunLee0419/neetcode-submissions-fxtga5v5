class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newNums = []
        multi_all = 1
        multi_all0 = 1
        counter = 0
        for element in nums: 
            multi_all*= element
            if element == 0:
                element = 1
                counter += 1

            multi_all0 *= element
            

        for i in range(len(nums)):
            print(i)
            if nums[i] == 0:
                if counter > 1:
                    newNums.append(multi_all)
                    continue
                newNums.append(multi_all0)
                continue

            newNums.append(int(multi_all/nums[i]))
        if counter == len(nums):
            return [0] * counter
        return newNums
