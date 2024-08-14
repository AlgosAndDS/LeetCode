class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if not min(strs):
            return ""
        for i in range(len(min(strs))):
            if max(strs)[i] != min(strs)[i]:
                return max(strs)[:i]
        return min(strs)[:]