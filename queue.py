# Queue using two stacks
class Queue:
    def __init__(self, s1=[], s2=[]):
        self.s1 = s1
        self.s2 = s2
    
    def enqueue(self, x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    def front(self):
        if not self.s2:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        print(self.s2[-1])
        
if __name__ == "__main__":
    # number of queries
    t = int(input().strip())
    q = Queue()
    
    #loop through queries
    for t_itr in range(t):
        s = input()
        if s[0] == '1':
            val = s.split(' ')[1]
            q.enqueue(val)
        elif s[0] == '2':
            q.dequeue()
        elif s[0] == '3':
            q.front()
            
