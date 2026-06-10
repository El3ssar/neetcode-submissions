class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}
        for elem in s:
            if elem in s_hash:
                s_hash[elem] += 1
            else:
                s_hash[elem] = 1
        for elem in t:
            if elem in t_hash:
                t_hash[elem] += 1
            else:
                t_hash[elem] = 1
        if s_hash.keys() != t_hash.keys():
            return False
        for elem in s_hash.keys():
            if s_hash[elem] != t_hash[elem]:
                return False
        return True