class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            l = [0] * 26 
            for j in strs[i]:
                l[ord(j) - ord('a')] += 1
            d[tuple(l)].append(strs[i])
        return list(d.values())     