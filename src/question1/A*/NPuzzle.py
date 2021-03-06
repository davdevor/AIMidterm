class Node:

    def __init__(self):
        self.grid = []
        self.heuristic = 0
        self.g = 0
        self.parent = None
        self.empty_col = -1
        self.empty_row = -1
        self.f = 0

    def copy_node(self, node):
        self.empty_row = node.empty_row
        self.empty_col = node.empty_col
        temp_grid = []
        for x in node.grid:
            temp_row = []
            for y in x:
                temp_row.append(y)
            temp_grid.append(temp_row)
        self.grid = temp_grid

    def swap_pos(self, pos1, pos2):
        temp = self.grid[pos1[0]][pos1[1]]
        self.grid[pos1[0]][pos1[1]] = self.grid[pos2[0]][pos2[1]]
        self.grid[pos2[0]][pos2[1]] = temp


class NPuzzle:

    def __init__(self):
        self.root = Node()
        self.goal = []
        self.n = -1

    def is_goal(self, node):
        return node.grid == self.goal

    def generate_states(self, node):
        states = []
        empty_col = node.empty_col
        empty_row = node.empty_row
        # check if empty is on corners
        # top left
        if empty_col == 0 and empty_row == 0:
            for x in range(2):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row, empty_col + 1])
            states[0].empty_row = empty_row
            states[0].empty_col = empty_col + 1
            states[1].swap_pos([empty_row, empty_col], [empty_row + 1, empty_col])
            states[1].empty_row = empty_row + 1
            states[1].empty_col = empty_col

        # bottom left
        elif empty_col == 0 and empty_row == self.n:
            for x in range(2):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row - 1, empty_col])
            states[0].empty_row = empty_row - 1
            states[0].empty_col = empty_col
            states[1].swap_pos([empty_row, empty_col], [empty_row, empty_col + 1])
            states[1].empty_row = empty_row
            states[1].empty_col = empty_col + 1

        # top right
        elif empty_row == 0 and empty_col == self.n:
            for x in range(2):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row, empty_col - 1])
            states[0].empty_row = empty_row
            states[0].empty_col = empty_col - 1
            states[1].swap_pos([empty_row, empty_col], [empty_row + 1, empty_col])
            states[1].empty_row = empty_row + 1
            states[1].empty_col = empty_col
        # bottom right
        elif empty_row == self.n and empty_col == self.n:
            for x in range(2):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row, empty_col - 1])
            states[0].empty_row = empty_row
            states[0].empty_col = empty_col - 1
            states[1].swap_pos([empty_row, empty_col], [empty_row - 1, empty_col])
            states[1].empty_row = empty_row - 1
            states[1].empty_col = empty_col
        # check edges
        # left edge
        elif empty_col == 0:
            for x in range(3):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row - 1, empty_col])
            states[0].empty_row = empty_row - 1
            states[0].empty_col = empty_col
            states[1].swap_pos([empty_row, empty_col], [empty_row + 1, empty_col])
            states[1].empty_row = empty_row + 1
            states[1].empty_col = empty_col
            states[2].swap_pos([empty_row, empty_col], [empty_row, empty_col + 1])
            states[2].empty_row = empty_row
            states[2].empty_col = empty_col + 1
        # top edge
        elif empty_row == 0:
            for x in range(3):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row, empty_col + 1])
            states[0].empty_row = empty_row
            states[0].empty_col = empty_col + 1
            states[1].swap_pos([empty_row, empty_col], [empty_row, empty_col - 1])
            states[1].empty_row = empty_row
            states[1].empty_col = empty_col - 1
            states[2].swap_pos([empty_row, empty_col], [empty_row + 1, empty_col])
            states[2].empty_row = empty_row + 1
            states[2].empty_col = empty_col
        # right edge
        elif empty_col == self.n:
            for x in range(3):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row - 1, empty_col])
            states[0].empty_row = empty_row - 1
            states[0].empty_col = empty_col
            states[1].swap_pos([empty_row, empty_col], [empty_row + 1, empty_col])
            states[1].empty_row = empty_row + 1
            states[1].empty_col = empty_col
            states[2].swap_pos([empty_row, empty_col], [empty_row, empty_col - 1])
            states[2].empty_row = empty_row
            states[2].empty_col = empty_col - 1
        # bottom edge
        elif empty_row == self.n:
            for x in range(3):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row, empty_col - 1])
            states[0].empty_row = empty_row
            states[0].empty_col = empty_col - 1
            states[1].swap_pos([empty_row, empty_col], [empty_row, empty_col + 1])
            states[1].empty_row = empty_row
            states[1].empty_col = empty_col + 1
            states[2].swap_pos([empty_row, empty_col], [empty_row - 1, empty_col])
            states[2].empty_row = empty_row - 1
            states[2].empty_col = empty_col
        # else it is in inside of grid
        else:
            for x in range(4):
                temp_node = Node()
                temp_node.copy_node(node)
                temp_node.parent = node
                temp_node.g = node.g + 1
                states.append(temp_node)
            states[0].swap_pos([empty_row, empty_col], [empty_row, empty_col - 1])
            states[0].empty_row = empty_row
            states[0].empty_col = empty_col - 1
            states[1].swap_pos([empty_row, empty_col], [empty_row, empty_col + 1])
            states[1].empty_row = empty_row
            states[1].empty_col = empty_col + 1
            states[2].swap_pos([empty_row, empty_col], [empty_row - 1, empty_col])
            states[2].empty_row = empty_row - 1
            states[2].empty_col = empty_col
            states[3].swap_pos([empty_row, empty_col], [empty_row + 1, empty_col])
            states[3].empty_row = empty_row + 1
            states[3].empty_col = empty_col

        return states

    # returns the path of how you got to the node passed in
    def path(self, node):
        path = []
        while node is not None:
            path.append(node.grid)
            node = node.parent
        path.reverse()
        return path

    # the A* search for the N-Puzzle
    def search_both(self):
        if self.is_goal(self.root):
            return self.path(self.root)
        q = [self.root]
        while len(q) != 0:
            current_node = q.pop(0)
            if self.is_goal(current_node):
                return self.path(current_node)

            states = self.generate_states(current_node)
            for z in range(len(states)):
                if self.is_goal(current_node):
                    return self.path(current_node)
                states[z].heuristic = self.heuristic_both(states[z])
                states[z].f = states[z].heuristic + states[z].g
                pos = self.find(q, states[z])
                if pos > -1:
                    if q[pos].f > states[z].f:
                        q[pos].f = states[z].f
                        q[pos].g = states[z].g
                        q[pos].heuristic = states[z].heuristic
                    continue
                else:
                    self.my_insort_left(q, states[z])

        return []

    # the A* search for the N-Puzzle
    def search(self):
        if self.is_goal(self.root):
            return self.path(self.root)
        q = [self.root]
        while len(q) != 0:
            current_node = q.pop(0)
            if self.is_goal(current_node):
                return self.path(current_node)

            states = self.generate_states(current_node)
            for z in range(len(states)):
                if self.is_goal(current_node):
                    return self.path(current_node)
                states[z].heuristic = self.heuristic(states[z])
                states[z].f = states[z].heuristic + states[z].g
                pos = self.find(q, states[z])
                if pos > -1:
                    if q[pos].f > states[z].f:
                        q[pos].f = states[z].f
                        q[pos].g = states[z].g
                        q[pos].heuristic = states[z].heuristic
                    continue
                else:
                    self.my_insort_left(q, states[z])

        return []

    # returns position of x in l, -1 if not in list
    def find(self, l, x):
        if len(l) == 0:
            return -1
        pos = 0
        while pos != len(l) and l[pos].grid != x.grid:
            pos += 1
        if pos == len(l):
            pos = -1
        return pos

    # used to insert into a sorted list into sorted position
    def my_insort_left(self, a, x, lo=0, hi=None):
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid].f < x.f:
                lo = mid + 1
            else:
                hi = mid
        a.insert(lo, x)

    def manhattan(self, coord1, coord2):
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    def linear_conflict(self, node):
        linearConflict = 0
        # vertical conflict
        for x in range(self.n + 1):
            max = -1
            for y in range(self.n + 1):
                value = node.grid[x][y]
                if value != 0 and int((node.grid[x][y] - 1) / (self.n + 1)) == x:
                    if value > max:
                        max = value
                    else:
                        linearConflict += 2
        for x in range(self.n + 1):
            max = -1
            for y in range(self.n + 1):
                value = node.grid[x][y]
                if value != 0 and int(value % (self.n + 1)) == y:
                    if value > max:
                        max = value
                    else:
                        linearConflict += 2
        return linearConflict

    # gets manhattan
    def heuristic(self, node):
        manhattan_sum = 0
        # determine manhattan distance
        for x in range(self.n + 1):
            for y in range(self.n + 1):
                x_pos = int(node.grid[x][y] / (self.n + 1))
                y_pos = (node.grid[x][y] % self.n + 1)
                manhattan_sum += self.manhattan([x, y], [x_pos, y_pos])
        return manhattan_sum

    # get manhattan and linear conflict combines
    def heuristic_both(self, node):
        manhattan_sum = 0
        linear = 0
        # determine manhattan distance
        for x in range(self.n + 1):
            for y in range(self.n + 1):
                x_pos = int(node.grid[x][y] / (self.n + 1))
                y_pos = (node.grid[x][y] % self.n + 1)
                manhattan_sum += self.manhattan([x, y], [x_pos, y_pos])
        linear = self.linear_conflict(node)
        return manhattan_sum + linear

    # read in puzzle with size n
    # initalize the root and goal state
    def initialize(self, filename):
        file = open(filename, mode='r')
        num = file.readline()
        n = int(num)
        temp_n = n
        n = int((n + 1) ** .5)
        self.n = n - 1
        nums = []
        for x in range(temp_n):
            nums.append(x + 1)
        nums.append(0)
        temp_goal = []
        for x in range(n):
            temp_row = []
            for x in range(n):
                temp_row.append(nums.pop(0))
            temp_goal.append(temp_row)
        self.goal = temp_goal

        line = file.readline()
        line = line.strip("\n")
        line = line.split(" ")
        temp_grid = []
        for x in range(n):
            temp_row = []
            for y in range(n):
                z = int(line.pop(0))
                if z == 0:
                    self.root.empty_row = x
                    self.root.empty_col = y
                temp_row.append(z)
            temp_grid.append(temp_row)
        self.root.grid = temp_grid
        file.close()
