# This problem was asked by Netflix.
# 
# Implement a queue using a set of fixed-length arrays.
# The queue should support enqueue, dequeue, and get_size operations.


class Queue:
    def __init__(self, arr_size = 0):
        self.arr        = []
        self.arr_size   = arr_size
        self.init_queue()
        
    def init_queue(self):
        for i in range(self.arr_size):
            self.arr.append([])  # I mean, I could add some "empty" indicator, such as "null" or 0, or "empty", but this way it literally handles empty spots
            
    def enqueue(self, val):
        for i in self.arr:
            if len(i) == 0:
                i.append(val)
                self.show()
                return  # if we found an empty slot, and we appended the value, lets just return
        print("Queue is full, cannot add: %s" % val)
                
        
    def dequeue(self):
        val = []
        if len(self.arr[0]) != 0:
            val = self.arr[0]  #this will be returned and dequeued
            
        for i, _ in enumerate(self.arr):
            if i != len(self.arr)-1:
                self.arr[i] = self.arr[i+1]  # keep shifting values to the left until we reach the end
            else:
                self.arr[-1] = []  # if we reached the end, set last value to empty
        self.show()
        return val
        
    def size(self):
        size = 0
        for i, _ in enumerate(self.arr):
            if len(self.arr[i]) != 0:
                size += 1
        print("Queue size: %s" % size)
        
    def show(self):
        print(self.arr)
        
q = Queue(5)
q.enqueue(3)
q.enqueue(5)
q.enqueue(1)
q.size()
q.enqueue(0)
q.enqueue(6)
q.dequeue()
q.enqueue(0)
q.dequeue()
q.enqueue(18)
q.enqueue("tele?")
q.enqueue(69420)
q.size()
q.dequeue()
q.dequeue()
q.enqueue(69420)
q.dequeue() 
q.dequeue()
q.dequeue()
q.dequeue()
q.size()
q.dequeue()