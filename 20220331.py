'''Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5],
it should become [1, 5, 2, 4, 3].

If the stack is [1, 2, 3, 4],
it should become [1, 4, 2, 3].
'''

N = 5


class LIFOStack:
    def __init__(self):
        self._stack = []
        self._size  = 0

    def push(self, val):
        self._stack.append(val)
        self._size += 1

    def pop(self):
        self._size -= 1
        return self._stack.pop()

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def top(self):
        return self._stack[-1]

    def show(self):
        return self._stack


class FIFOQueue:
    def __init__(self):
        self._s1 = []
        self._s2 = []

    def enq(self, val):
        while len(self._s1) != 0:
            self._s2.append(self._s1.pop())

        self._s1.append(val)

        while len(self._s2) != 0:
            self._s1.append(self._s2.pop())

    def deq(self):
        return self._s1.pop()

    def show(self):
        return self._s1

    def size(self):
        return len(self._s1)

# - instanciating the stack, and queue
orig_stack  = LIFOStack()
other_queue = FIFOQueue()

# - creating original stack
for i in range(1,N+1):
    orig_stack.push(i)
print("Initial stack: %s" % orig_stack.show())

# - performing the task
# -- first, we enqueue every element of the original stack, except the bottom one
for _ in range(N-1):
    other_queue.enq(orig_stack.pop())

# -- then we push the last element, then shift the queue as many times as how long the queue is, minus 1.
# -- This ensures the top 2 element of the queue is the next smallest, and next highest element
# -- We double-dequeue these elements. Unless we only have 1 element left, in which case we just single-dequeue. Unless the queue is empty, in which case we're done
while True:
    if other_queue.size() == 0:
        break

    orig_stack.push(other_queue.deq())

    for _ in range(other_queue.size()-1):
        other_queue.enq(other_queue.deq())

    if other_queue.size() > 1:
        orig_stack.push(other_queue.deq())

print("Modified stack: %s" % orig_stack.show())

