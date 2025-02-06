class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while(True):
            n -=2**int(math.log(n, 2))
            sum+=1
            if (n == 0):
                break
        return sum