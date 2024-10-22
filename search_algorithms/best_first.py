# NAME : TOFIK AHMED SAYID
#  ID : 1743/14
# SUBJECT : FUDAMENTALS OF ARTIFIAL INTELLIGENCE
# COURSECODE : SENG 4082
# =============================================
"""(BFS) algorithm is a heuristic search algorithm that expands the node that appears to be closest to the goal based on a given heuristic function; Two common heuristics used in this case are:

Misplaced Tile Heuristic=> Counts how many tiles are not in their goal position.
Manhattan Distance Heuristic => Measures the total distance each tile is from its goal position."""

import heapq

# Node class to store the state, parent, action, cost, and heuristic
class Node:
    def __init__(self, state, parent, action, cost, heuristic):
        self.state = state      # The current state (position)
        self.parent = parent    # The parent node (from where this node is generated)
        self.action = action    # Action taken to reach this node (e.g., move up, move down)
        self.cost = cost        # The total path cost to reach this node
        self.heuristic = heuristic  # Heuristic value estimating the closeness to the goal

    # Comparison method for priority queue (based on heuristic)
    def __lt__(self, other):
        return self.heuristic < other.heuristic

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

# Function to calculate the misplaced tile heuristic
def misplaced_tile_heuristic(state, goal_state):
    return sum(1 for i in range(len(state)) if state[i] != 0 and state[i] != goal_state[i])

# Function to expand a node and generate all possible child nodes
def expand_node(node, goal_state):
    expanded_nodes = []
    # Try all possible moves (up, down, left, right) and add valid states
    for action, move in [('Up', move_up), ('Down', move_down), ('Left', move_left), ('Right', move_right)]:
        new_state = move(node.state)
        if new_state:
            # Calculate the heuristic value for the new state
            heuristic = misplaced_tile_heuristic(new_state, goal_state)
            expanded_nodes.append(Node(new_state, node, action, node.cost + 1, heuristic))  # Cost + 1 for each move
    return expanded_nodes

# Best-First Search Algorithm using Misplaced Tile Heuristic
def best_first_search(start_state, goal_state):
    # Priority queue (min-heap) to store nodes based on the heuristic value
    frontier = []
    initial_heuristic = misplaced_tile_heuristic(start_state, goal_state)
    heapq.heappush(frontier, Node(start_state, None, None, 0, initial_heuristic))  # Push the start node with heuristic

    explored = set()  # Set to store explored states

    while frontier:
        # Get the node with the lowest heuristic value
        current_node = heapq.heappop(frontier)

        # If the goal state is found, return the path and the cost
        if current_node.state == goal_state:
            return get_solution_path(current_node), current_node.cost

        # Mark the current state as explored
        explored.add(tuple(current_node.state))

        # Expand the current node and add the valid child nodes to the frontier
        for child in expand_node(current_node, goal_state):
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

    # Run Best-First Search
    solution, cost = best_first_search(start_state, goal_state)

    if solution is not None:
        print("\nSolution found:")
        print(" -> ".join(solution))
        print("Number of moves:", len(solution))
        print("Total cost:", cost)
    else:
        print("No solution found.")
