class Solution:
    def longestValidParentheses(self, s: str) -> int:
        countl = 0
        countr = 0
        maxx = 0
        for i in range(len(s)):
            if (s[i] == '('):
                countl+=1
            else:
                countr+=1
                if (countr > countl):
                    maxx = max(maxx,(countr - 1) * 2)
                    countl = 0
                    countr = 0
                if (countr == countl):
                    maxx = max(maxx, countr*2)
        
        countr2 = 0
        countl2 = 0
        maxx2 = 0
        for i in range(len(s)-1,-1,-1):
            if (s[i] == ')'):
                countr2+=1
            else:
                countl2+=1
                if (countl2 > countr2):
                    maxx2 = max(maxx2,(countl2 - 1) * 2)
                    countl2 = 0
                    countr2 = 0
                if (countr == countl):
                    maxx = max(maxx, countl*2)
        
        maxxf = max(maxx, maxx2)
        return maxxf