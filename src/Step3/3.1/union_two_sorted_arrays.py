'''
Problem statement
Given two sorted arrays, ‘a’ and ‘b’, of size ‘n’ and ‘m’, respectively, return the union of the arrays.



The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order.



Note: 'a' and 'b' may contain duplicate elements, but the union array must contain unique elements.



Example:
Input: ‘n’ = 5 ‘m’ = 3
‘a’ = [1, 2, 3, 4, 6]
‘b’ = [2, 3, 5]

Output: [1, 2, 3, 4, 5, 6]

Explanation: Common elements in ‘a’ and ‘b’ are: [2, 3]
Distinct elements in ‘a’ are: [1, 4, 6]
Distinct elements in ‘b’ are: [5]
Union of ‘a’ and ‘b’ is: [1, 2, 3, 4, 5, 6]
'''

def sortedArray(a: list[int], b: list[int]) -> list[int]:
    i = 0
    j = 0
    l = []
    before = -1
    while (i!= len(a) or j!= len(b)):
        if (i == len(a)):
            if (b[j] != before):
                l.append(b[j])
                before = b[j]
            j+=1
        elif (j == len(b)):
            if (a[i] != before):
                l.append(a[i])
                before = a[i]
            i+=1
        else:
            if (a[i] < b[j]):
                if (a[i] != before):
                    l.append(a[i])
                    before = a[i]
                i+=1
                continue
            else:
                if (b[j] != before):
                    l.append(b[j])
                    before = b[j]
                j+=1
                continue            
    return l

# Time complexity: O(m+n)
# Space complexity: O(m+n)
# Two pointer approach
