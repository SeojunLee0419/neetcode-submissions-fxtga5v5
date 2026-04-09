class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #cant remove elements as time complexity can be o(n) but space is also o(n)
        numbers.sort()
        
        if numbers[-1] + numbers[0] > target:
            numbers.pop(-1)
            
        start = 0
        end = len(numbers)-1
        left = 0
        right = 0
        for i, n in enumerate(numbers):
            start = left
            end = len(numbers) - right -1

            if numbers[start] + numbers[end] == target:
                lst = [start+1, end+1]
                return lst

            #if n>= target: 
                #break;
            if numbers[start] + numbers[end]> target:
                right+=1
            elif numbers[start] + numbers[end] < target:
                left+= 1
            
            
        
            