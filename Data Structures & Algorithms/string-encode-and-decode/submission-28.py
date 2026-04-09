class Solution:

    def encode(self, strs: List[str]) -> str:
        # if len(strs) == 0:
        #     return "zero"
        # msg = ""
        if not strs:
            return ""
        sz, res = [], ""
        for words in strs:
            sz.append(len(words))
        for s in sz:
            res+= str(s)
            res+= ","
        res+= "#"
        for s in strs: 
            res+= s
        return res

    def decode(self, s: str) -> List[str]:
        # if s == "zero":
        #     decoded = "".split()
        #     return decoded
        
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
        
        