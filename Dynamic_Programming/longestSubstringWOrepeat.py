# SLIDING WINDOW

# Time: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
  # Time: O(2n) = O(n)
 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {} # CONSIDER    using counter
        begin = end = 0
        ls = 0 # length of longest substring
        
        if not s:
            return 0
        
        while end < len(s):
            if s[end] not in hash_map:
                hash_map[s[end]] = 1
            else:
                hash_map[s[end]] += 1
            while(hash_map[s[end]] > 1):
                hash_map[s[begin]] -= 1
                begin += 1      
            if end-begin > ls:
                ls = end-begin
            end += 1
        return ls+1
