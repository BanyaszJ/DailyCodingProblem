'''You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.'''
 
# let f be 0 and t be 1 for simplicity
class Board():
    def __init__(self):
        self.board =   [[0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0]]
                        
        self.start  = []
        self.end    = []
        
                        
    def set_start(self, start):
        self.start = start
        print("Start set to %s" % self.start)
        
    def set_end(self, end):
        self.end = end
        print("End set to %s" % self.end)
        
    def get_start(self):
        return self.start
        
    def get_end(self):
        return self.end
        
    def get_board(self):
        return self.board    
        
        
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
        
        
class A_solver():
    def __init__(self):
        self.start  = []
        self.end    = []
        self.board  = []
    
    def get_start(self, start):
        self.start = start
        return self.start
        
    def get_end(self, end):
        self.end = end
        return self.end
        
    def get_board(self, board):
        self.board = board
        return board
        
    def solve(self, board):
        print("Solving for start: %s " % self.start)
        print("Solving for end: %s " % self.end)
        print("Solving for board: %s" % self.board)
        
        start_node  = Node(parent = None, position = (self.start[0], self.start[1]))
        end_node   = Node(parent = None, position = (self.end[0],     self.end[1]))
        
        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:
            # print(open_list)
            # print(closed_list)

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path

            # Generate children
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(self.board) - 1) or node_position[0] < 0 or node_position[1] > (len(self.board[len(self.board)-1]) -1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if self.board[node_position[0]][node_position[1]] != 0:
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)
        
board = Board()
board.set_start([3,1])
board.set_end([3,3])

a_solver = A_solver()
a_solver.get_start(board.get_start())
a_solver.get_end(board.get_end())
a_solver.get_board(board.board)

result = a_solver.solve(board)
print("\n===== RESULT =====")
print(result)
print("Total of %s steps" % len(result))
