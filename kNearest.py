import math
from scipy import spatial
    
class Solution:


    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        tree = spatial.KDTree(points)
		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=K, p=2) 
        return [points[i] for i in idx] if K > 1 else [points[idx]]
    
    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)
    
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Perform the QuickSelect algorithm on the list"""
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        # Return the first k elements of the partially sorted list
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        """Partition the list around the pivot value"""
        pivot = self.choose_pivot(points, left, right)
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            # Iterate through the range and swap elements to make sure
            # that all points closer than the pivot are to the left
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        # Ensure the left pointer is just past the end of
        # the left range then return it as the new pivotIndex
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left
    
    def choose_pivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
        """Choose a pivot element of the list"""
        return points[left + (right - left) // 2]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the list with a custom comparator function
        points.sort(key=self.squared_distance)
        
        # Return the first k elements of the sorted list
        return points[:k]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
        

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sort by distance
        # return first k
        close = {}
        near = []
        
        for i, p in enumerate(points):
            close[i] = p[0]**2+p[1]**2
        
        for i in sorted(close.items(), key=lambda item: item[1]):
            if len(near) > k:
                break
            near.append(points[i[0]])
        print(near)
        
        return near[:k]       
        
        '''
        
