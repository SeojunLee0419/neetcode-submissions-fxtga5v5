class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, j in enumerate(nums):
            if j not in hash_map:
                hash_map[j] = []
            hash_map[j].append(i)
        print(hash_map)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff == nums[i] and len(hash_map[diff]) == 1:
                continue
            if diff in hash_map:
                print(f"{diff} exists")
                counter = 0
                while counter < len(hash_map[diff]): 
                    idx = hash_map[diff][counter]  
                    if idx != i:
                        break
                    counter +=1
            
                list = [i, idx]
                list.sort()
                return list
