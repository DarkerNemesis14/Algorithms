class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashS = set()
        
        i = 0
        for j in range(len(s)):
            while s[j] in hashS:
                hashS.remove(s[i])
                i += 1
            hashS.add(s[j])
            l = max(l, j - i + 1)

        return l