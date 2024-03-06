from typing import *
import math
def generate(numRows: int) -> List[List[int]]:
    l = []
    for i in range(numRows):
        l.append([])
        j=0
        while (j <=i):
            l[i].append(math.comb(i,j))
            j+=1

    return l

print(generate(5))

def generate2(numRows: int) -> List[List[int]]:
    l = []
    for i in range(numRows):
        l.append([])
        j=0
        while (j<=i):
            if (j!=0 and j!=i):
                l[i].append(l[i-1][j] + l[i-1][j-1])
            else:
                l[i].append(1)
            j+=1
    return l

# Time complexity: O(n^2)
# Space complexity: O(n^2)

# To optimise operations, can calculate actual value of a combination for a element in row iteratively, multiplying and dividing a number at a time 
# as we move through row. Just makes the combination answer code more optimal.
# e.g. for 5th row, 1st element = 1, 2nd element = 4/1, 3rd element = 2nd element * 3/2, 4th element = 3rd element * 2/3. 5th element = 1