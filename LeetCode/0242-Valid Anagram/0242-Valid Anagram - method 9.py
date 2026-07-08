class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=(s.lower()).replace(" "."")
        t=(t.lower()).replace(" "."")
        count=[0]*26
        for char in s:
            count[ord(char)-ord('a')]+=1
        for char in t:
            count[ord(char)-ord('a')]=-1
            