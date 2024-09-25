# 8_puzzle_problem
8-Puzzle Solver using Greedy Best-First Search
Overview
This project implements a solution to the classic 8-puzzle problem using the Greedy Best-First Search algorithm with the Manhattan Distance heuristic. The goal of the 8-puzzle is to move the tiles around on a 3x3 grid until they match the goal configuration.

The problem is defined by:

1) Initial State: A starting arrangement of the tiles.
2) Goal State: The desired final arrangement of the tiles.
3) Empty Tile (0): This represents the blank space used for swapping adjacent tiles.

The Manhattan Distance heuristic calculates the distance between the current state and the goal state by summing the distances of all tiles from their correct positions.

How It Works
Greedy Best-First Search
The Greedy Best-First Search (GBFS) algorithm is a heuristic search algorithm that always selects the next state which appears to be closest to the goal. It uses the Manhattan distance to guide its selection, prioritizing states with the smallest heuristic value.

Key Components
1) Manhattan Distance Heuristic: This heuristic is used to estimate how close the current puzzle state is to the goal state by summing the Manhattan distances (absolute differences in the x and y coordinates) of each tile from its goal position.

2) Puzzle Class: Encapsulates the functionality of the 8-puzzle problem, including:

Generating possible moves (swapping the blank space with adjacent tiles).
Finding the blank tile's location.
Backtracking from the goal state to find the sequence of steps (solution path).

3) State Representation: States are represented as 2D lists (3x3 matrices), with the value 0 representing the blank tile.

4) Priority Queue: A priority queue is used to store and retrieve the next state to explore based on the Manhattan distance heuristic.

Functions
1) manhattan_distance(state, goal): Calculates the total Manhattan distance between the current state and the goal state.
2) generate_moves(state): Generates all possible new states by moving the blank tile (up, down, left, or right).
3) trace_path(came_from, current_state): Traces back the path from the goal state to the initial state using a dictionary of parent states.
4) greedy_best_first_search(): Implements the GBFS algorithm to solve the puzzle.
Requirements
This project uses Python's standard library, and no external libraries are required except for heapq for the priority queue implementation.

Usage
Puzzle Input
The initial and goal states are defined as 2D lists, where each list contains three sub-lists of integers (representing the 3x3 puzzle).
