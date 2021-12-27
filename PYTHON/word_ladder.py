class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
    '''
    

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        
        # keep track of count in word dictionary
        # add begin word to Q
        # pop word from Q, loop through wordList
        # if word in wordList is one character away, add to Q, add previous count
        
        distance = {}
        Q =[]
        
        distance[beginWord] = 0
        Q.append(beginWord)
        
        while Q:
            target = Q.pop(0)
            for w in wordList:
                diff = 0
                for i in range(len(w)):
                    if w[i] != target[i]:
                        diff += 1
                if diff == 1:
                    if w == endWord:
                        return distance[target] +1
                    Q.append(w)
                    distance[w] = distance[target] +1
                
        return 0
        '''