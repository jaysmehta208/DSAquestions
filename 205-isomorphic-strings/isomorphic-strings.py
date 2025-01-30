class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        s2 = ""
        d1 = {}
        for i in range(len(s)):
            d1[s[i]] = t[i]
        dups = list(d1.values())
        if (len(set(dups)) < len(dups)):
            return False
        for j in range(len(s)):
            s2+=d1[s[j]]
        return t==s2
        
