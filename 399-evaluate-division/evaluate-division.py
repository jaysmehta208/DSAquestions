class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1/values[i]))
        ans = []
        print(adj)
        for i in range(len(queries)):
            if queries[i][0] not in adj or queries[i][1] not in adj:
                ans.append(-1)
                continue
            if queries[i][0] == queries[i][1]:
                ans.append(1)
                continue
            queue = deque()
            queue.append((queries[i][0], 1))
            # mult = 1
            visited = {queries[i][0]}
            flag=0
            while(len(queue)!=0):
                tup = queue.popleft()
                visited.add(tup[0])
               
                # mult *= tup[1]
                if (queries[i][1] == tup[0]):
                    ans.append(tup[1])
                    flag = 1
                    break
                    # if (i == 2):
                    #     print("found")
                    #     print(visited)
                    #     print(queue)
                    # break
                else:
                    # if (i == 2):
                    #     print("outside")
                    #     print(visited)
                    #     print(queue)
                    for j in adj[tup[0]]:
                        if j[0] not in visited:
                            
                            queue.append((j[0],j[1]*tup[1]))
                            visited.add(j[0])
                    # if (i == 2):
                    #     print("inside")
                    #     print(visited)
                    #     print(queue)
            if flag:
                continue
            ans.append(-1)
        return ans

                

        return []