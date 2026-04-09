class Solution:

    def encode(self, strs: List[str]) -> str:

        sizes, res = [], ""
        for element in strs: 
            sizes.append(len(element))
            
        for element in sizes: 
            res += str(element )
            res += ","
        res+= "#"
        for element in strs:
            res+= element

        return res


    def decode(self, s: str) -> List[str]:
        
        res = []
        instruction = []
        
        idx = s.find("#")
        s_info = s[:idx]
        s_content = s[idx+1:]
    
        # num = ""
        # for ch in s_info:
        #     if ch == ",":
        #         instruction.append(num)
        #         res = ""
        #         continue
        #     num += ch
        instruction = s_info.split(",")
        del instruction[-1]

        length1 = 0
        length2 = 0
        for element in instruction: 
            length2 += int(element)
            res.append(s_content[length1:length2])
            length1 = length2

        

        return res

            
        
        