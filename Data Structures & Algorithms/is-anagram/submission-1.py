class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sting1 = list(s)
        string2 = list(t)

        for ch in sting1:
            if ch in string2:
                string2.remove(ch)

            else:
                return False
        
        return True