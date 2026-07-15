
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={')':'(',']':'[','}':'{'}
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1]!=hashmap[c]:
                    return False
                stack.pop()
        return not bool(stack)
            
