# The Hamming weight of a string is the number of symbols that are different from the zero-symbol of the alphabet used. 
# It is thus equivalent to the Hamming distance from the all-zero string of the same length. 
# For the most typical case, a string of bits, this is the number of 1's in the string, or the digit sum of the 
# binary representation of a given number and the ℓ₁ norm of a bit vector. 
# In this binary case, it is also called the population count, popcount, sideways sum, or bit summation.

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            c += 1
            n &= (n -1)
        return c


class Solution:
    def hammingWeight(self, n):
        n = (n & (0x55555555)) + ((n >> 1) & (0x55555555))
        n = (n & (0x33333333)) + ((n >> 2) & (0x33333333))
        n = (n & (0x0f0f0f0f)) + ((n >> 4) & (0x0f0f0f0f))
        n = (n & (0x00ff00ff)) + ((n >> 8) & (0x00ff00ff))
        n = (n & (0x0000ffff)) + ((n >> 16) & (0x0000ffff))
        return n
      
# Dynamic Solutions

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans 

class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0]*(n+1)
        
        for i in range(n+1):
            ret[i] = str(bin(i)).count('1')
          
        return ret
class Solution:
    
    def popcount(self, x: int) -> int:
        c = 0
        while x:
            c += 1
            x &= (x -1)
        return c
    
    def countBits(self, n: int) -> List[int]:
        ret = [0]*(n+1)
        
        for i in range(n+1):
            
            ret[i] = self.popcount(i)
            
        return ret
      
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1) 
        return ans 
