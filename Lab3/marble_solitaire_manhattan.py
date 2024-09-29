import time
import heapq

class Marble:
    def __init__(self, state=[[2,2,1,1,1,2,2],[2,2,1,1,1,2,2],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[2,2,1,1,1,2,2],[2,2,1,1,1,2,2]], g=0, h = 0, path=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.path = path if path is not None else []

    def __lt__(self, other):
        return self.f < other.f

goal = [
    [2,2,0,0,0,2,2],
    [2,2,0,0,0,2,2],
    [0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0],
    [2,2,0,0,0,2,2],
    [2,2,0,0,0,2,2]
]

directions = [
    (0, -2), 
    (0, 2),
    (2, 0),
    (-2, 0),
]

def displayBoard(state):
    for row in state:
        print(row)

# manhattan distance
def calculate_h(state):
    manhattan_distance = 0
    for i in range(7):
        for j in range(7):
            if state[i][j] == 1:
                #since center is (3, 3)
                manhattan_distance += abs(i - 3) + abs(j - 3)
    return manhattan_distance

def calculate_g(state):
    count = 0
    for i in range(7):
        for j in range(7):
            if state[i][j] == 1:
                count += 1
    return count

def check_possibility(state, i, j, x, y):
    if 0 <= i + x < 7 and 0 <= j + y < 7:
        middle_i = i + x // 2
        middle_j = j + y // 2
        if state[middle_i][middle_j] == 1 and state[i + x][j + y] == 0:
            return True
    return False

def next_state(state, i, j, x, y):
    new_state = [row[:] for row in state]
    middle_i = i + x // 2
    middle_j = j + y // 2
    new_state[i][j] = 0
    new_state[middle_i][middle_j] = 0
    new_state[i + x][j + y] = 1
    return new_state

def getSuccessors(node):
    successors = []
    for i in range(7):
        for j in range(7):
            if node.state[i][j] == 1:
                for x, y in directions:
                    if check_possibility(node.state, i, j, x, y):
                        new_state = next_state(node.state, i, j, x, y)
                        child = Marble(new_state, 
                                       g=calculate_g(new_state), 
                                       h = calculate_h(new_state), 
                                       path=node.path + [(i, j, i+x, j+y)])
                        successors.append(child)
    return successors

def goalTest(state):
    return state == goal

def BestFS():
    Total_nodes_expanded = 0
    start_node = Marble()
    frontier = []
    explored = set()

    heapq.heappush(frontier, (start_node.f, start_node))
    while frontier:
        _, curr = heapq.heappop(frontier)
        Total_nodes_expanded += 1

        if goalTest(curr.state):
            print("Total nodes expanded: ", Total_nodes_expanded)
            return curr

        curr_state_tuple = tuple(map(tuple, curr.state))
        explored.add(curr_state_tuple)

        for successor in getSuccessors(curr):
            successor_state_tuple = tuple(map(tuple, successor.state))
            if successor_state_tuple not in explored:
                heapq.heappush(frontier, (successor.f, successor))

    print("Total nodes expanded: ", Total_nodes_expanded)
    return None


print("Search started")
start_time = time.time()
node = BestFS()
end_time = time.time()
elapsed_time = end_time - start_time

print("Time taken: ", elapsed_time)
displayBoard(node.state)
