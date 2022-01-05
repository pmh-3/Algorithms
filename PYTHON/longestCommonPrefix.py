class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = len(min(strs, key=len))
        low = 1
        high = min_len
        while low <= high:
            mid = (low + high)//2
            prefix = strs[0][:mid]
            if all(s.startswith(prefix) for s in strs[1:]):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:(low + high)//2]
