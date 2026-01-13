class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())
