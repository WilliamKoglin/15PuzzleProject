# 15 Puzzle Solver using A*

## Overview
An implementation of the A* Search and Breadth First Search algorithm to solve the 15-puzzle game.

BFS was used as a baseline to prepare for A* Search and is unrefined

## How to run
Run ASolve.py in the correct directory and input your puzzle left to right top to bottom with 0 representing the blank. The program will output the tiles needed to be moved in order.

## Features
- Manhattan distance heuristic
- Priority queue based search
- Solution path reconstruction
- Solvability checking

## Algorithm
f(n) = g(n) + h(n)

g(n): moves taken from initial state
h(n): Manhattan distance from solved position

## Example

Initial:
[1,2,3,4,
 5,6,7,8,
 9,10,0,12,
 13,14,11,15]

Solution:
[11,15]

## Limitations
Currently optimized for moderate difficulty puzzles.
Difficult states may require more memory/time.

Future improvements:
- Linear conflict heuristic
- Pattern databases
- Improved duplicate state handling
- Improvements to optimal path rebasing between explored nodes

- MAKE TEST CASES!!!

Development reopened to implement IDA* due to memory concerns in full stack deployment
