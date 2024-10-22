# NAME : TOFIK AHMED SAYID
#  ID : 1743/14
# SUBJECT : FUDAMENTALS OF ARTIFIAL INTELLIGENCE
# COURSECODE : SENG 4082
#=========================================
import heapq

# Node class to store the state, parent, cost, and action taken
class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state      # The current state (position)
        self.parent = parent    # The parent node (from where this node is generated)
        self.action = action    # Action taken to reach this node (e.g., move up, move down)
        self.cost = cost        # The total path cost to reach this node

    # Comparison method for priority queue (based on cost)
    def __lt__(self, other):
        return self.cost < other.cost

# Function to display the current board
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
    index = new_state.index(0)  # Find the index of the blank space (0)
    if index not in [0, 1, 2]:  # If blank is not in the top row, we can move it up
        new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
        return new_state
    return None

def move_down(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [6, 7, 8]:  # If blank is not in the bottom row, we can move it down
        new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
        return new_state
    return None

def move_left(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 3, 6]:  # If blank is not in the first column, we can move it left
        new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
        return new_state
    return None

def move_right(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [2, 5, 8]:  # If blank is not in the last column, we can move it right
        new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
        return new_state
    return None

# Function to expand a node and generate all possible child nodes
def expand_node(node):
    expanded_nodes = []
    # Try all possible moves (up, down, left, right) and add valid states
    for action, move in [('Up', move_up), ('Down', move_down), ('Left', move_left), ('Right', move_right)]:
        new_state = move(node.state)
        if new_state:
            expanded_nodes.append(Node(new_state, node, action, node.cost + 1))  # Cost is incremented by 1 for each move
    return expanded_nodes

# Uniform Cost Search Algorithm
def uniform_cost_search(start_state, goal_state):
    # Priority queue (min-heap) to store nodes based on the least cost
    frontier = []
    heapq.heappush(frontier, Node(start_state, None, None, 0))  # Push the start node with 0 cost

    explored = set()  # Set to store explored states

    while frontier:
        # Get the node with the lowest cost
        current_node = heapq.heappop(frontier)

        # If the goal state is found, return the path and the cost
        if current_node.state == goal_state:
            return get_solution_path(current_node), current_node.cost

        # Mark the current state as explored
        explored.add(tuple(current_node.state))

        # Expand the current node and add the valid child nodes to the frontier
        for child in expand_node(current_node):
            if tuple(child.state) not in explored:
                heapq.heappush(frontier, child)  # Add the child node to the frontier

    return None, None  # If no solution is found

# Function to retrieve the solution path from the goal node to the start node
def get_solution_path(node):
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    return path[::-1]  # Reverse the path since we are tracing it back from goal to start

# Main function
if __name__ == "__main__":
    # Define the start state and the goal state
    start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # 0 represents the blank space
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Display the starting board and the goal board
    print("Starting State:")
    display_board(start_state)
    print("Goal State:")
    display_board(goal_state)

    # Run Uniform Cost Search
    solution, cost = uniform_cost_search(start_state, goal_state)

    if solution is not None:
        print("\nSolution found:")
        print(" -> ".join(solution))
        print("Number of moves:", len(solution))
        print("Total cost:", cost)
    else:
        print("No solution found.")
