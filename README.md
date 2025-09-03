# This project is a compiltion of algorthms and data stcrutures in Python (and C++ later on)

## Implemented ALgorithms:
- Sorting: insertion sort, merge sort, quicksort (Lomuto partition)
- Searching: linear search, binary search (iterative)
- Data structures: Stack (LIFO), Queue (FIFO), Deque, simple LinkedList (optional)
- Graphs: BFS, DFS (for traversal & shortest path in unweighted graphs)
- Stretch (later): Heap + heapsort, Union-Find (for Kruskal), Dijkstra, Counting/Radix.

### Visualization

* For visualization I used Streamlit for a MVP (single‑file UI)
##### The basic strcuture is:

-> app.py – 3 tabs, one page:

1. Tab 1 – Sorting Visualizer:
- Controls: array size, shuffle, step speed, algorithm select
- Show bars changing per step; counters for comparisons/swaps

2. Tab 2 – Stacks & Queues

- Buttons: push/pop/enqueue/dequeue; show list/diagram arrows
- Tiny explainer: LIFO vs FIFO vs LILO

3. Tab 3 – Graphs
- Build small graph (n≤10), run BFS/DFS, show visit order and parents