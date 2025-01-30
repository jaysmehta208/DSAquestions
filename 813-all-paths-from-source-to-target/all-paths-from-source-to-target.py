class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(value, visited): 
            visited.append(value)
            if (value == len(graph) - 1):
                answer.append(visited.copy())
                visited.pop()
                return
            for i in graph[value]:
                dfs(i, visited)
            visited.pop()
        visited = []
        answer = []
        dfs(0, visited)
        return answer

