'''You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (0, 3), (2, 1), (4, 4), (3, 1), (1, 0)]


(0,0)-> 1xx2xx
        6xxxxx
        x3xxxx
        x5xxxx
        xxxx4x <-(4,6)

Output: 13

better idea:
visualize only two points, with the first point being (0, 0) and ghe second point being (x,y)
reduce target x,y by one (x-1, y-1) to simulate moving in a diagonal, each step corresponding to 1 step
once a value reaches 0 (ex.: (0, y)), keep reducing the remaining value (here: y) until it reaches (0,0)
the number of total steps taken will be the shortest path between two points
store value, and make (x,y) the new (0,0), and the next value (x,y)
repeat until end of list

'''

path = [(0, 0), (0, 3), (2, 1), (4, 4), (3, 1), (1, 0)]

class ShortestPath():
    def __init__(self, zero, end):
        self.zeropoint  = list(zero)
        self.endpoint   = list(end)

    def calc_new_endpoint(self):
        self.endpoint[0] = abs(self.endpoint[0] - self.zeropoint[0])
        self.endpoint[1] = abs(self.endpoint[1] - self.zeropoint[1])
        
    def steps(self):        
        return max(self.endpoint)
    
sum = 0    
for i,j in enumerate(path):
    if i == 0: continue # ignore 1st step
    short = ShortestPath(path[i-1], path[i])
    short.calc_new_endpoint()
    sum += short.steps()
print(sum)

