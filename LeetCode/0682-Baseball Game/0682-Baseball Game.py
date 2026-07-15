
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops=[]
        for i in operations:
            if i=='C':
                ops.pop()
            elif i=='D':
                ops.append(2*ops[-1])
            elif i=='+':
                ops.append(ops[-1]+ops[-2])
            else:
                ops.append(int(i))
        return sum(ops)