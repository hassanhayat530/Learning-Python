# Learning Python

A collection of beginner Python assignments. Each file is a standalone script that runs on its own, with no dependencies beyond the Python 3 standard library and no other files from this repository.

## Basic Programs

| File | Description |
|---|---|
| `Range of years.py` | Reads a start year and an end year (1600 to 2100) and prints the total number of days in that range, accounting for Gregorian leap years. |
| `Good Numbers.py` | Reads a positive integer N and counts how many numbers from 1 to N are divisible by each of their own digits. Solved without arrays, strings, or char variables. |
| `Caesar Cypher.py` | Reads a key K and a line of text, then encrypts it with a Caesar cipher. Output is uppercase, non-letters are unchanged, and keys beyond 25 or below -25 wrap around. A negative key decrypts. |
| `Hot Dogs.py` | Reads customers' maximum prices and prints the price that maximizes revenue, choosing the lowest price if there is a tie. |
| `Copying by Sentences.py` | Reads text made of sentences ending in periods and prints each sentence on its own line, joining sentences split across lines with a single space. |
| `Fractions.py` | Defines a `Fraction` class with `add`, `sub`, `mul`, `div`, and `__repr__`, then uses it to evaluate one arithmetic expression per input line. Division by zero prints `invalid`. |
| `Merging Sorted Files.py` | Merges two sorted files into a third without loading them fully into memory. The optional `-i` flag makes the merge case-insensitive. |
| `Soduko.py` | Reads a 9x9 Sudoku grid and prints how many rows, columns, and 3x3 blocks are invalid (0 means a valid solution). |
| `same.py` | Defines a `Node` class and a `same` function that checks whether two binary trees have identical structure and values. |

## Algorithms and Data Structures

| File | Description |
|---|---|
| `Prime Factorization.py` | Reads an integer N (at least 2) and prints its prime factorization, such as `2^3 * 3 * 5^2`. Efficient enough for large inputs. |
| `Number of occurences in ordered array.py` | Reads a sorted sequence and a list of search values, then prints how many times each value occurs. Uses an efficient search instead of counting one by one, and no dictionaries. |
| `circular_queue.py` | Defines a `CircularQueue` class backed by an array, with `enqueue`, `dequeue`, `count`, and `avg`. The array doubles in size when it fills up, and `collections` is not used. |
| `solver.py` | Defines a `solve` function that searches any state space and returns the shortest path from a start state to a goal state, or `None` if there is no path. |
| `Cycle in a Graph.py` | Reads a directed graph and prints the length and vertices of a cycle, or `neni` if the graph is acyclic. |

## Running

Most scripts read from standard input and write to standard output:

```bash
python3 "Range of years.py"
```

Three scripts work differently:

- `Merging Sorted Files.py` takes command-line arguments: `python3 "Merging Sorted Files.py" [-i] input1 input2 output`
- `same.py`, `circular_queue.py`, and `solver.py` have no input or output code. They only define classes or functions, so import them to test them, for example `from same import Node, same`.

## Notes

These assignments were written for an automatic grader, so the input scripts read input without printing prompts.
