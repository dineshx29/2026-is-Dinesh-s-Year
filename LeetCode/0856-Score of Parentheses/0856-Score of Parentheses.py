
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for ch in s:
            if ch=='(':
                stack.append(0)
            else:
                value=stack.pop()
                if value==0:
                    stack[-1]+=1
                else:
                    stack[-1]+=2*value
        return stack[0]