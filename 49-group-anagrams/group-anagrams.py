class Solution(object):
    def groupAnagrams(self, strs):
        out = defaultdict(list)
        for i in strs :
            x = ''.join(sorted(i))
            out[x].append(i)
        return list(out.values())
        