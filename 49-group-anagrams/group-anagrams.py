class Solution(object):
    def groupAnagrams(self, strs):
        out = defaultdict(list)
        for word in strs:
            # count frequency of each character
            count = [0] * 26  
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            # use tuple as key (hashable)
            out[tuple(count)].append(word)
        return list(out.values())