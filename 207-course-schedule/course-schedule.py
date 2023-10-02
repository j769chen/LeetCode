class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def canFinishHelper(node):
            if len(graph[node]) == 0:
                return True
            if node in visited:
                return False
            visited.add(node)
            for n in graph[node]:
                if canFinishHelper(n) == False:
                    return False
 
            visited.remove(node)
            graph[node] = []
        
            return True
                    
            
        graph = {}
        
        for i in range(numCourses):
            graph[i] = []
        
        for i in range(len(prerequisites)):
            if prerequisites[i][0] in graph:
                graph[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                graph[prerequisites[i][0]] = [prerequisites[i][1]]
        
        visited = set()
        for i in range(numCourses):
            if canFinishHelper(i) == False:
                return False
        
        return True
                
        
    
    