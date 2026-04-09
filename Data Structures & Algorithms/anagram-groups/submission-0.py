class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        st = dict()
        for i,v in enumerate(strs):
            arr= [0]*26
            for letter in v:
                arr[ord('z')-ord(letter)]+=1

            arr = tuple(arr)

            if arr not in st:
                st[arr] = [v]
            else:
                st[arr].append(v)

        print(st)

        res = []
        for values in st.values():
            res.append(values)

        return res
            

        # list_idx = []
    
        # for i, w in enumerate(list_of_hash):
        #     a = [] 
        #     for i in range(len(list_of_hash)):
        #         if w in list_of_hash[i]:
        #             a.append(i)
        #     list_idx.append(a)
        
        
                    
                


        