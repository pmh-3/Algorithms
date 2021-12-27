# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        ret = []
        level = [root]
        
        while root and level:
            current = []
            nxtLvl = []
            
            
            for n in level:
                current.append(n.val)
           
                if n.right:
                    nxtLvl.append(n.right)
                if n.left:
                    nxtLvl.append(n.left)

            ret.append(current)
            level = nxtLvl
        
            
        for i, l in enumerate(ret):
            if i%2 == 0:
                l = l.reverse()
                
        return ret
    
        '''
      
      def zigzagLevelOrder(self, root):
        if not root: return []
        queue = deque([root])
        result, direction = [], 1
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level[::direction])
            direction *= (-1)
        return result
        
        
        ZZlevels = []
        if not root:
            return ZZlevels
        
        def helper(root, l):
            if l == len(ZZlevels):
                ZZlevels.append([])
            
            ZZlevels[l].append(root.val)
            # if odd, right to left
            if l%2 == 0:
                if root.right:
                    helper(root.right, l+1)
                if root.left:
                    helper(root.left, l+1)
            else:
                if root.left:
                    helper(root.left, l+1)
                if root.right:
                    helper(root.right, l+1)
            
        helper(root, 0)
        return ZZlevels
        '''