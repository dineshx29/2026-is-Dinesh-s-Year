class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=(s.lower()).replace(" "."")
        t=(t.lower()).replace(" "."")
        count=[0]*26
        