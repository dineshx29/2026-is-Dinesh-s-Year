
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for words in strs:
            counts=[0]*26
            for char in words:
                char=char.lower()
                counts[ord(char)-ord('a')]+=1
            key=tuple(counts)
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(words)
        return list(hashmap.values())        