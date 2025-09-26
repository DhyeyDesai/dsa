# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/description/

# INTUITION:
# 1. This builds on Course Schedule I - we need both cycle detection AND ordering
# 2. We use DFS post-order traversal to get topological ordering
# 3. Key insight: add course to result AFTER processing all its prerequisites
# 4. This ensures prerequisites appear before the course that needs them

# ALGORITHM BREAKDOWN:
# - Same cycle detection as Course Schedule I using 'cycle' set
# - Add 'visit' set to track completely processed nodes (optimization)
# - Use post-order DFS: process dependencies first, then add current course
# - Result naturally gives us valid topological order

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list: course -> prerequisites
        depMap = {i: [] for i in range(numCourses)}
        result = []
        
        for course, preReq in prerequisites:
            depMap[course].append(preReq)
        
        # Two sets for different purposes:
        visit = set()    # Completely processed nodes (optimization)
        cycle = set()    # Nodes in current DFS path (cycle detection)
        
        def dfs(course):
            # Cycle detected: course is in current exploration path
            if course in cycle:
                return False
            
            # Already processed this course completely - skip
            if course in visit:
                return True
            
            # Mark as currently being explored (for cycle detection)
            cycle.add(course)
            
            # Process all prerequisites first (DFS deeper)
            for prereq in depMap[course]:
                if not dfs(prereq):
                    return False  # Cycle found in prerequisite chain
            
            # Done exploring this path - remove from cycle detection
            cycle.remove(course)
            
            # Mark as completely processed
            visit.add(course)
            
            # POST-ORDER: Add course AFTER all prerequisites are processed
            # This ensures prerequisites appear before courses that need them
            result.append(course)
            return True
                        
        # Process all courses to ensure we get complete ordering
        for course in range(numCourses):
            if not dfs(course):
                return []  # Cycle found - no valid ordering exists
        
        return result  # Valid topological ordering