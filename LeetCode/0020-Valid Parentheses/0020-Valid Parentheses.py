
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={')':'(',']':'[','}':'{'}
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack: #sees empty or not
                    return False
                if stack[-1]!=hashmap[c]: # match with top element 
                    return False
                stack.pop()  # since both matched - it pops the bracket 
        return not bool(stack) # size of the stack - empty/not