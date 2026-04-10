class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        nums.sort()
        
        for i, val in enumerate(nums):

            if i>0 and val == nums[i-1]: #to avoid duplicate
                continue
            
            l, r = i+1, len(nums)-1

            while l < r:
                
                if val+ nums[l] + nums[r] > 0: 
                    r-=1
                elif val + nums[l] + nums[r] < 0: 
                    l+=1
                else: 
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1 #both have to be moved inward; doesn't work if only one of them move
                         # Shouldn't negelct any cases as if it were to reach zero after moving either l or r inward,
                         # it would just be a duplicate 
                    while nums[l] == nums[l-1] and l<r: #to avoid duplicate
                                                        #ex. test case 19 nums=[-2,0,0,2,2]
                                                        #using only the top(l+=1, r-=1) isn't good enough 
                        l+=1
                    
        return res