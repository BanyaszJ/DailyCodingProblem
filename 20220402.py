'''Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.'''
# Joci's note: this would be a tad bit boring in python, so I'm gonna do it twice, the second solution gonna be with a queue

K = 3
l = [1,2,3,4,5,6,7]

'''
# With list
for _ in range(K):
    l.insert(0, l[-1])
    l.pop()
'''    

# With queue:
class Queue:
    def __init__(self, l):
        self.q = l
        self.q2 = []
        
    def enq(self, val):
        while len(self.q) != 0:
            self.q2.append(self.q.pop())
            
        self.q.append(val)
        
        while len(self.q2) != 0:
            self.q.append(self.q2.pop())
            
    def deq(self):
        return self.q.pop()
        
    def show(self):
        return self.q
        
q = Queue(l)
for _ in range(K):
    q.enq(q.deq())

print(q.show())
