class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        for x,y in intervals:
            if not res or x>res[-1][1]:
                res.append([x, y])
            else:
                res[-1][1]=max(res[-1][1],y)