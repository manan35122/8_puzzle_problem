import heapq

# Manhattan Distance Heuristic Function
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Exclude the empty tile (0)
                x, y = divmod(state[i][j] - 1, 3)  # Get goal position of current tile
                distance += abs(i - x) + abs(j - y)
    return distance

# Define the 8-Puzzle Problem as a class
class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    # Find the location of the blank (0) tile
    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    # Generate possible moves from current state
    def generate_moves(self, state):
        x, y = self.find_blank(state)
        moves = []
        directions = [('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)]
        for direction, dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Create new state by swapping the blank with the adjacent tile
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                moves.append(new_state)
        return moves

    # Trace back the path from goal to the initial state
    def trace_path(self, came_from, current_state):
        path = []
        while current_state:
            path.append(current_state)
            current_state = came_from.get(tuple(tuple(row) for row in current_state))
        path.reverse()
        return path

    # Greedy Best-First Search Algorithm
    def greedy_best_first_search(self):
        # Priority queue to store the states along with their heuristic cost
        priority_queue = []
        heapq.heappush(priority_queue, (manhattan_distance(self.initial_state, self.goal_state), self.initial_state))
        
        # Set to store visited states
        visited = set()
        visited.add(tuple(tuple(row) for row in self.initial_state))
        
        # Dictionary to store the parent of each state
        came_from = {tuple(tuple(row) for row in self.initial_state): None}
        
        while priority_queue:
            # Get the state with the lowest heuristic value (Greedy)
            _, current_state = heapq.heappop(priority_queue)
            
            # If the goal is reached, return the solution
            if current_state == self.goal_state:
                print("Solution found!")
                return self.trace_path(came_from, current_state)
            
            # Generate new possible states
            for new_state in self.generate_moves(current_state):
                new_state_tuple = tuple(tuple(row) for row in new_state)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    heapq.heappush(priority_queue, (manhattan_distance(new_state, self.goal_state), new_state))
                    came_from[new_state_tuple] = current_state  # Keep track of the parent state
        
        print("No solution found.")
        return None
# Function to print the puzzle state
def print_puzzle(state):
    for row in state:
        print(row)
    print()

initial_state = [
    [1, 3, 4],
    [8, 6, 2],
    [7, 0, 5]
]

# Goal state
goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]



# Create Puzzle instance and solve
puzzle = Puzzle(initial_state, goal_state)
solution_path = puzzle.greedy_best_first_search()

# Print the solution steps
if solution_path:
    print("Steps to solve the puzzle:")
    for i, step in enumerate(solution_path):
        print(f"Step {i}:")
        print_puzzle(step)