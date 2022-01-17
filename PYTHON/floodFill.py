class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def neighbors(r,c):
            u,d,l,r=(r+1,c),(r-1,c),(r,c-1),(r,c+1)
            return [v for v in [u,d,l,r] if isValid(v)]

        def isValid(pixel):
            r,c = pixel
            if r < len(image) and r >= 0 and c< len(image[0]) and c>=0 and image[r][c] == trgtColor:
                return True
            return False
        
        trgtColor = image[sr][sc]
        if newColor == trgtColor:
            return image
        Q = []
        Q.append((sr,sc))
    
        while Q:
            r, c = Q.pop(0)
            image[r][c] = newColor
            for n in neighbors(r,c):
                Q.append(n)
        return image
    
# DFS
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
