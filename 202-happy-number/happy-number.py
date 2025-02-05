class Solution:
    def isHappy(self, n: int) -> bool:
        
        l = [n]
        while(True):
            summ = 0
            for i in str(n):
                summ+= int(i)**2
            if (summ == 1):
                return True
            if (summ in l):
                return False
            l.append(summ)
            
            n = summ
        return False
        