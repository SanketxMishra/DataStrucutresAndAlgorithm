class Solution(object):
    def topKFrequent(self, nums, k):
        out = {}
        ret = []
        
        # Special case: only one number
        if len(nums) == 1:
            return nums
        
        # Count frequencies
        for i in nums:
            if i in out:
                out[i] += 1
            else:
                out[i] = 1
        
        # Sort dictionary by frequency (descending)
        dict_sorted = sorted(out.items(), key=lambda item: item[1], reverse=True)
        
        # Pick top k elements
        for i in range(k):
            ret.append(dict_sorted[i][0])
        
        return ret
