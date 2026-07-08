            counts[ord(char)-ord('a')]+=1
        for char in t:
            counts[ord(char)-ord('a')]-=1
        for count in counts:
            if count!=0:
                return False
        return True
        for char in s:
        counts=[0]*26