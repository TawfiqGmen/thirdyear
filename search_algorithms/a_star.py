# NAME : TOFIK AHMED SAYID
#  ID : 1743/14
# SUBJECT : FUDAMENTALS OF ARTIFIAL INTELLIGENCE
# COURSECODE : SENG 4082
# ===============================================
import heapq

# Node class for storing the state, parent, action, cost (g), and heuristic (h)
class Node:
    def __init__(self, state, parent, action, cost, heuristic):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost  # g(n) - Actual cost to reach this node
        self.heuristic = heuristic  # h(n) - Heuristic value
        self.total_cost = cost + heuristic  # f(n) = g(n) + h(n)

    # Comparison method for priority queue (based on f(n))
    def __lt__(self, other):
        return self.total_cost < other.total_cost

# Function to display the 8-puzzle board
def display_board(state):
    print("-------------")
    print("| %i | %i | %i |" % (state[0], state[1], state[2]))
    print("-------------")
    print("| %i | %i | %i |" % (state[3], state[4], state[5]))
    print("-------------")
    print("| %i | %i | %i |" % (state[6], state[7], state[8]))
    print("-------------")

# Move functions (up, down, left, right) for generating new states
def move_up(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 1, 2]:  # Can move up if blank is not in top row
        new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
        return new_state
    return None

def move_down(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [6, 7, 8]:  # Can move down if blank is not in bottom row
        new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
        return new_state
    return None

def move_left(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 3, 6]:  # Can move left if blank is not in the first column
        new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
        return new_state
    return None

def move_right(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [2, 5, 8]:  # Can move right if blank is not in the last column
        new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
        return new_state
    return None

# Manhattan distance heuristic
def manhattan_distance_heuristic(state, goal_state):
    distance = 0
    for i, value in enumerate(state):
        if value != 0:  # Ignore the blank space
            goal_index = goal_state.index(value)
            # Calculate the Manhattan distance
            distance += abs(goal_index // 3 - i // 3) + abs(goal_index % 3 - i % 3)
    return distance

# Expand a node to generate possible moves and new states
def expand_node(node, goal_state):
    expanded_nodes = []
    for action, move in [('Up', move_up), ('Down', move_down), ('Left', move_left), ('Right', move_right)]:
        new_state = move(node.state)
        if new_state:
            heuristic = manhattan_distance_heuristic(new_state, goal_state)
            expanded_nodes.append(Node(new_state, node, action, node.cost + 1, heuristic))
    return expanded_nodes

# A* Search algorithm
def a_star_search(start_state, goal_state):
    # Priority queue (min-heap) to store nodes based on f(n) = g(n) + h(n)
    frontier = []
    initial_heuristic = manhattan_distance_heuristic(start_state, goal_state)
    heapq.heappush(frontier, Node(start_state, None, None, 0, initial_heuristic))  # Push the start node

    explored = set()  # Set to store explored states

    while frontier:
        # Get the node with the lowest total cost (f(n))
        current_node = heapq.heappop(frontier)

        # If the goal state is found, return the solution and cost
        if current_node.state == goal_state:
            return get_solution_path(current_node), current_node.cost

        explored.add(tuple(current_node.state))

        # Expand the current node and add valid child nodes to the frontier
        for child in expand_node(current_node, goal_state):
            if tuple(child.state) not in explored:
                heapq.heappush(frontier, child)

    return None, None  # No solution found

# Retrieve the solution path from the goal node to the start node
def get_solution_path(node):
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    return path[::-1]  # Reverse the path to get from start to goal

# Main function
if __name__ == "__main__":
    # Define the start state and goal state
    start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # 0 represents the blank space
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Display the start and goal state boards
    print("Starting State:")
    display_board(start_state)
    print("Goal State:")
    display_board(goal_state)

    # Run the A* Search
    solution, cost = a_star_search(start_state, goal_state)

    if solution is not None:
        print("\nSolution found:")
        print(" -> ".join(solution))
        print("Number of moves:", len(solution))
        print("Total cost:", cost)
    else:
        print("No solution found.")
