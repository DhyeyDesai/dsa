# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depMap = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            depMap[course].append(preReq)
        
        visit = set()
        
        def dfs(n):
            if depMap[n] == []:
                return True
            if n in visit:
                return False
            else:
                visit.add(n)
                for dep in depMap[n]:
                    if not dfs(dep):
                        return False
                visit.remove(n)
                depMap[n] = []
                return True
                        
                    
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
                
            