# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = {i:[] for i in range(numCourses)}
        result = []
        for course, preReq in prerequisites:
            depMap[course].append(preReq)
        
        visit = set()
        cycle = set()
        
        def dfs(n):
            if n in cycle:
                return False
            if n in visit:
                return True
            else:
                cycle.add(n)
                for dep in depMap[n]:
                    if not dfs(dep):
                        return False
                cycle.remove(n)
                visit.add(n)
                result.append(n)
                return True
                        
                    
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result