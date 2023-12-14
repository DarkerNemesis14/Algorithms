class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        hashS = dict()
        hashT = dict()

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        for l in t:
            if l not in hashS or hashS[l] != hashT[l]:
                return False
        
        return True