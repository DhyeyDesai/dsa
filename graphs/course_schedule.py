# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

# INTUITION:
# 1. This is a cycle detection problem in a directed graph (topological sort)
# 2. If there's a cycle in prerequisites, it's impossible to complete all courses
# 3. We use DFS to detect cycles by tracking the current path we're exploring
# 4. Key insight: if we revisit a node in our current path, we found a cycle

# ALGORITHM BREAKDOWN:
# - Build adjacency list: course -> list of prerequisites
# - For each course, DFS through its prerequisite chain
# - Track visited nodes in current path to detect cycles
# - Use memoization: once a course is confirmed safe, mark it as having no deps

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a dependency map adjacency list: course -> prerequisites
        depMap = {i: [] for i in range(numCourses)}
        for course, preReq in prerequisites:
            depMap[course].append(preReq)
        
        # Track nodes in current DFS path (for cycle detection)
        visit = set()
        
        def dfs(course):
            # Base case: course has no prerequisites (safe to take)
            if depMap[course] == []:
                return True
            
            # Cycle detected: we're revisiting a course in current path
            if course in visit:
                return False
            
            # Mark current course as being explored in this path
            visit.add(course)
            
            # Check all prerequisites recursively
            for prereq in depMap[course]:
                if not dfs(prereq):
                    return False  # Found cycle in prerequisite chain
            
            # Backtrack: remove from current path (we're done exploring this branch)
            visit.remove(course)
            
            # Optimization: mark as "no dependencies" to avoid future recomputation
            depMap[course] = []
            return True
                        
        # Check every course to ensure no cycles exist
        for course in range(numCourses):
            if not dfs(course):
                return False  # Cycle found - impossible to complete
        
        return True  # No cycles found - all courses can be completed
                
            