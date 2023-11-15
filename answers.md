# CMPS 2200 Recitation 10## Answers

**Name:** Jack Zemke


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?
    - Each node is visited exactly once, thanks to the lines
        ```
        if here in result:
            # print('already visited ',here)
            continue```
    - Each edge is traversed once. The additional work done at each node is constant, simply updating the appropriate lists. Therefore the work of this implimentation is $O(n + m)$

- **4)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?
    - **Once** for an undirected graph. If the graph is connected, then it won't matter what node you call `reachable` on since the list of reachable nodes will match the list of all nodes at the end of the call. On the other hand if the graph is not connected, it wont matter which node you call `reachable` on because no matter what the list of reachable nodes will *not* match the list of all nodes in the graph.

- **5)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?
    - `Connected` calls `reachable` once, which has work $O(n + m)$. Additionally, there is a for loop in the line `nodes = sorted([i for i in graph])` which has a work of $O(n)$. Therefore, `connected` has a work of $O(n + m + n) = O(2n+m) \approx O(n+m)$

- **7)**
    - The work of the algorithm would not change. The same steps would apply, where you explore all connected nodes from an arbitrary starting node then explore any leftover nodes (unconnected from the starting node) and their siblings/children until there are no unvisited nodes left, keeping a running tally of the number of connected groups exist within the graph.
