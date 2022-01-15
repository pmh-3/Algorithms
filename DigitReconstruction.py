# If your coding for longer than expected, you may have missed a trick
# leave no stone unturned!!!
class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        res += "0"*s.count('z')
        res += "1"*(s.count('o')-s.count('z')-s.count('w')-s.count('u'))
        res += "2"*s.count('w')
        res += "3"*(s.count('h') - s.count('g'))
        res += "4"*s.count('u')
        res += "5"*(s.count('f') - s.count('u'))
        res += "6"*s.count('x')
        res += "7"*(s.count('s')-s.count('x'))
        res += "8"*s.count("g")
        res += "9"*(s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res
      
class Solution:
    def originalDigits(self, s: str) -> str:

        digitChar = ['zero','one', 'two', 'three','four', 'five', 'six','seven','eight','nine']
        
        
        chFound = ''
        digFound = []
        
        for i, n in enumerate(digitChar):
            # all chars of digit are found in s
            if self.containsAll(s,n):
                digFound.append(i)
                chFound += n
        # remove all characters from s in chFound
        for ch in s:
            if ch in chFound:
                chFound = chFound.replace(ch, '', 1)
        # find remining digits in chFound
        if len(chFound)>0:
            for i, n in enumerate(digitChar):
                # all chars of digit are found in chFound
                if self.containsAll(chFound,n):
                    chFound.remove(i)
                # remove all characters from chFound in n
                for ch in n:
                    if ch in chFound:
                        chFound = chFound.replace(ch, '', 1)
        # sort and return
        digFound.sort()
        ret = ''
        for d in digFound:
            ret += str(d)
            
        return ret
    
    def containsAll(self, str, set):
        for c in set:
            if c not in str: return 0
        return 1
