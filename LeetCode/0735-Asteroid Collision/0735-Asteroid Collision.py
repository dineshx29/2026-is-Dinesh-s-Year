
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for num in asteroids:
            if num>0: # possitive nos
                stack.append(num)
            else:
                while stack and stack[-1]>0 and -num>stack[-1]:
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(num)
                elif stack[-1]==-num:
                    stack.pop()
        return stack
                
