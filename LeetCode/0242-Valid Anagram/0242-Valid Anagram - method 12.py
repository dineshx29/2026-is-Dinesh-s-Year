        s=(s.lower())
        t=(t.lower()).replace(" "."")
        count=[0]*26
        for char in s:
            count[ord(char)-ord('a')]+=1
        for char in t:
            count[ord(char)-ord('a')]=-1
        for count in counts:
            if count!=0:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        