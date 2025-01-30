class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # d = {}
        d = [0]*(len(words))
        count = 0
        for i in range(len(words)):
            if words[i][0] in 'aeiou' and words[i][len(words[i])-1] in 'aeiou':
                count+=1
                d[i] = count
            else:
                d[i] = count
        l = []
        for i in range(len(queries)):
            index1 = queries[i][0]
            index2 = queries[i][1]
            if index1 == 0:
                l.append(d[index2])
            else:
                l.append(d[index2] - d[index1 - 1])
        return l


