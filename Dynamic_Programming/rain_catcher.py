#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    areas += max_l - height[l]
                l +=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r]
                r -=1
        return areas
        

        
        
        
        '''

        rain = 0
        size = len(height)
        left_max = right_max = [None]*size
        
        left_max[0] = height[0]
        # store left max in array
        for i in range(1,size):
            left_max[i] = max(height[i],left_max[i-1])
            
        # store right max
        right_max[size-1] = height[size-1]
        for i in range(size-2,0):
            right_max[i] = max(height[i], right_max[i+1])
            
        # take minimum, subtract height
        for i in range(1,size-1):
            rain += min(right_max[i], left_max[i])-height[i]
            
        return rain
        
        
                rain = 0
        left = right = 0
 
        for i in height:

            
            # find left
            for l in height[i:0:-1]: 
                left = max(i,left)
            
            for r in height[i:len(height):1]:
                right = max(i,right)
                
            rain += min(left,right)-i
                
        return rain
        
        '''
