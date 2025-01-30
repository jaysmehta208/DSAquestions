# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(temp, count, answer):
            count+=1
            if (temp.left == None and temp.right == None):
                print("hello")
                answer = min(count, answer)
                return answer
            a1 = 10**6
            a2 = 10**6
            if (temp.left != None):
                a1 = dfs(temp.left, count, answer)
            if (temp.right != None):
                a2 = dfs(temp.right, count, answer)
            return min(a1,a2)
        answer = 10**6
        temp = root
        count = 0
        if (temp == None):
            return 0

        answer = dfs(temp, count, answer)
        return answer
