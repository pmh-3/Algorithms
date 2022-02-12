class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        return self.dfs(nums,[])
        
    def dfs(self, nums, path):
        # check if last number in path is valid
        for n in path:
            if n % path[-1] != 0 and path[-1]%n != 0:
                return path[:-1]
        ret = path
        # add val
        for i in range(len(nums)):
            p = self.dfs(nums[i+1:], path + [nums[i]])
            if len(p) > len(ret):
                ret = p
        return ret
