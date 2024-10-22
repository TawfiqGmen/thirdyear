# NAME : TOFIK AHMED SAYID
#  ID : 1743/14
# SUBJECT : FUDAMENTALS OF ARTIFIAL INTELLIGENCE
# COURSECODE : SENG 4082

#=======================================================
"""=> DFS simply follows paths deeply and may find a solution, but it doesn't minimize the number of moves.
=>  The first solution DFS finds could be far from the shortest or most efficient.
=>  DFS may backtrack over vast areas of the search space, leading to high move counts before reaching the goal."""

# Importing deque from collections module to implement DFS with stack
from collections import deque

# Node class to represent each state in the search tree
class Node:
    def __init__(self, state, parent, action, depth):
        # State represents the current configuration of the puzzle
        self.state = state
        # Parent points to the node that generated this node
        self.parent = parent
        # Action is the move made to get to this node (up, down, left, right)
        self.action = action
        # Depth represents the number of moves made from the start state to reach this node
        self.depth = depth

# Function to display the 8-puzzle board in a readable format
def display_board(state):
    """Displays the 8-puzzle board in a grid format."""
    print("-------------")
    print("| %i | %i | %i |" % (state[0], state[1], state[2]))
    print("-------------")
    print("| %i | %i | %i |" % (state[3], state[4], state[5]))
    print("-------------")
    print("| %i | %i | %i |" % (state[6], state[7], state[8]))
    print("-------------")

# Function to move the blank tile (0) up, down, left, or right
def move(state, direction):
    """Moves the blank tile in the given direction and returns the new state."""
    new_state = state[:]
    index = new_state.index(0)  # Find the position of the blank tile (0)

    # Define movement logic for each direction
    if direction == 'up' and index not in [0, 1, 2]:  # Move up (if not in the top row)
        new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
    elif direction == 'down' and index not in [6, 7, 8]:  # Move down (if not in the bottom row)
        new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
    elif direction == 'left' and index not in [0, 3, 6]:  # Move left (if not in the leftmost column)
        new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
    elif direction == 'right' and index not in [2, 5, 8]:  # Move right (if not in the rightmost column)
        new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
    else:
        return None  # Return None if the move is not possible

    return new_state  # Return the new state after the move

# Function to expand the current node and generate all possible moves
def expand_node(node):
    """Expands the current node and generates all possible child nodes."""
    directions = ['up', 'down', 'left', 'right']  # All possible directions
    expanded_nodes = []

    # Generate new nodes for each valid move
    for direction in directions:
        new_state = move(node.state, direction)
        if new_state is not None:
            # Create a new node with the new state, current node as the parent, and the action taken
            expanded_nodes.append(Node(new_state, node, direction, node.depth + 1))

    return expanded_nodes  # Return the list of expanded nodes

# Depth-First Search (DFS) function
def dfs(start_state, goal_state):
    """Performs DFS to find the solution path from the start state to the goal state."""
    # Initialize the start node
    start_node = Node(start_state, None, None, 0)

    # Stack (LIFO) to keep track of nodes to be explored
    frontier = deque([start_node])

    # Set to keep track of explored states (to avoid revisiting)
    explored = set()

    while frontier:
        # Pop the top node (the current node to explore)
        current_node = frontier.pop()

        # If the current state is the goal, return the solution path
        if current_node.state == goal_state:
            return solution_path(current_node)

        # Mark the current state as explored
        explored.add(tuple(current_node.state))

        # Expand the current node to generate child nodes (possible moves)
        for child in expand_node(current_node):
            # If the child state has not been explored and is not in the frontier, add it
            if tuple(child.state) not in explored and child not in frontier:
                frontier.append(child)

    return None  # Return None if no solution is found

# Function to reconstruct the solution path by tracing the parent nodes
def solution_path(node):
    """Reconstructs the solution path by tracing back from the goal node to the start node."""
    path = []
    while node.parent is not None:
        path.insert(0, node.action)  # Insert the action that led to this node
        node = node.parent  # Move to the parent node
    return path  # Return the list of actions (solution path)

# Main function to run the DFS algorithm
def main():
    # Define the start and goal states of the 8-puzzle
    start_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Initial state (you can modify this)
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]   # Goal state

    # Display the start and goal states
    print("Starting State:")
    display_board(start_state)
    print("Goal State:")
    display_board(goal_state)

    # Run DFS and get the result (solution path)
    result = dfs(start_state, goal_state)

    # Print the result
    if result is None:
        print("No solution found.")
    elif result == []:
        print("Start node is the goal state!")
    else:
        print("Solution found:", result)
        print("Number of moves:", len(result))

# Entry point of the script
if __name__ == "__main__":
    main()
