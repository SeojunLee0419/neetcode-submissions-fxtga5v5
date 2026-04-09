class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        s =s.lower()

        cleaned = ""
        for ch in s: 
            if ch.isalnum():
                cleaned+= ch
                print(cleaned)
        
        r_s = cleaned[::-1]

        if cleaned == r_s:
            return True
        return False
